import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Patient, User,History
from django.db import IntegrityError
import qrcode
import os
from pathlib import Path
import uuid
from pyzbar import pyzbar
from PIL import Image



def index(request):
    return render(request, 'hospital/index.html')



def login_view(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hospital/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "hospital/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hospital/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "hospital/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hospital/register.html")



@login_required(login_url='/login')
def patient_page(request):
    if request.user.is_authenticated:
        return render(request, "hospital/patients.html")
    else:
        return HttpResponseRedirect(reverse("login"))


@login_required(login_url='/login')
def add_patient(request):
    if request.method == 'GET':
        return render(request, "hospital/add_patient.html")
    elif request.method == 'POST':
        for key, value in request.POST.items():
            if value == '':
                return render(request, "hospital/add_patient.html", {
                    "message": "All fields are required."
                })
        qr_img = qrcode.make(f'{request.POST["email"]}')
        BASE_DIR = Path(__file__).resolve().parent.parent
        qr_uid = str(uuid.uuid4())
        qr_img.save(os.path.join(BASE_DIR, 'media/qr_codes', f'{qr_uid}.png'))
        image = request.FILES['image']
        patient = Patient(
            user = request.user,
            name = request.POST['fname'] + ' ' + request.POST['lname'],
            gender = request.POST['gender'],
            age = request.POST['birthday'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            address = request.POST['address'],
            blood_group = request.POST['blood'],
            job = request.POST['occ'],
            next_of_kin = request.POST['nextofkin'],
            next_of_kin_phone = request.POST['nextofkinp'],
            user_from = request.POST['country'],
            image = image,
            qr_code=f'/media/qr_codes/{qr_uid}.png'
        )
        patient.save()
        patient = Patient.objects.get(qr_code=f'/media/qr_codes/{qr_uid}.png')
        return HttpResponseRedirect(reverse("patient_detail", args=(patient.id,)))


@login_required(login_url='/login')
def browse(request):
    return render(request, "hospital/browse.html")


@login_required(login_url='/login')
def all_patients(request):
    patient = Patient.objects.all()
    pars = [post.serialize() for post in patient]
    pages = Paginator(pars, 10)
    page_obj = pages.get_page(request.GET.get('page'))
    return JsonResponse({
        "patients":page_obj.object_list,
        "num_pages":pages.num_pages,

    },safe=False)


@login_required(login_url='/login')
def serach(request,data):
    patient = Patient.objects.filter(name__icontains=data)
    pars = [post.serialize() for post in patient]
    pages = Paginator(pars, 10)
    page_obj = pages.get_page(request.GET.get('page'))
    return JsonResponse({
        "patients":page_obj.object_list,
        "num_pages":pages.num_pages,

    },safe=False)


@login_required(login_url='/login')
def patient_detail(request,id):
    patient = Patient.objects.get(id=id)
    history = History.objects.filter(patient=patient)
    print(history)
    return render(request, "hospital/patient_detail.html", {
        "patient":patient,
        "histories":history
    })



@login_required(login_url='/login')
def add_history(request,id):
    if request.method == 'POST':
        patient = Patient.objects.get(id=id)
        history = History.objects.filter(patient=patient)
        for key, value in request.POST.items():
            if value == '':
                return render(request, "hospital/patient_detail.html", {
                    "message": "All fields are required.",
                    "patient":patient,
                    "histories":history
                })
        history = History(
            patient = patient,
            date = request.POST['date'],
            diagnosis = request.POST['diagnosis'],
            description = request.POST['description'],
            treatment = request.POST['treatment'],
            user = request.user
        )
        history.save()
        return HttpResponseRedirect(reverse("patient_detail", args=(id,)))
   




@login_required(login_url='/login')
def delete_history(request,id):
    history = History.objects.get(id=id)
    history.delete()
    return HttpResponseRedirect(reverse("patient_detail", args=(history.patient.id,)))




@login_required(login_url='/login')
def read_page(request):
    return render(request, "hospital/read.html")


@login_required(login_url='/login')
def read_qr(request):
    if request.method == 'POST':
        image = request.FILES['image']
        de_image = Image.open(image)
        qr_decode = pyzbar.decode(de_image)
        if qr_decode:
            for data in qr_decode:
                email = data.data.decode('utf-8')
                patient = Patient.objects.get(email=email)
                return HttpResponseRedirect(reverse("patient_detail", args=(patient.id,)))
        else : 
            return render(request, "hospital/read.html", {
                     "message": "QR code not Matched."
                 })
       