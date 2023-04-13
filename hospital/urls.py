from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("patients", views.patient_page, name="patients"),
    path("add/patient", views.add_patient, name="add_patient"),
    path('browse',views.browse,name='browse'),
    path('allpatients',views.all_patients,name='all_patients'),
    path('patient/<str:data>',views.serach,name='serach'),
    path('patient/p/<int:id>',views.patient_detail,name='patient_detail'),
    path('add/history/<int:id>',views.add_history,name='add_history'),
    path('delete_history/<int:id>',views.delete_history,name='delete_history'),
    path('read',views.read_page,name='read'),
    path('readqr',views.read_qr,name='readqr'),
 ] 


