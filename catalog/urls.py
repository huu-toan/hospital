from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pro', views.pro, name='pro'),
    path('for_patient', views.for_patient, name='for_patient'),
    path('introduce', views.introduce, name='introduce'),
    path('doctors/', views.doctors, name='doctors'),
    path('search/', views.search, name='search'),
    path('patient_form', views.patient_form, name='patient_form'),
    path('success', views.success, name='success'),
    path('doctorinfo/<int:id>/', views.doctorinfo, name='doctorinfo'),
    path('doctorimage/<int:id>/', views.doctorimage, name='doctormage'),
]
