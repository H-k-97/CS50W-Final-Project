from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    pass


class Patient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    blood_group = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=50)
    next_of_kin_phone = models.CharField(max_length=50)
    user_from = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    qr_code = models.CharField(max_length=500,)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Birthday': self.age,
            'gender': self.gender,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'blood_group': self.blood_group,
            'job': self.job,
            'next_of_kin': self.next_of_kin,
            'next_of_kin_phone': self.next_of_kin_phone,
            'user_from': self.user_from,
            'image': self.image.url,
            'qr_code': self.qr_code

        }

        
    def __str__(self):
        return f"{self.id}  | {self.name} | {self.age} " 

class History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    description = models.TextField(max_length=500)
    diagnosis = models.CharField(max_length=50)
    treatment = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.id}  | Patient ID {self.patient} | {self.date} "