from telnetlib import STATUS
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    name = models.CharField(
        max_length=255, help_text=_('Enter a patient name'))
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    citizen_id = models.CharField(max_length=20)
    medical_record = models.FileField(upload_to='medical_records/')
    disease_type = models.CharField(max_length=255)
    status = models.BooleanField(
        default=False,
        help_text=_('Check the patient medical appointment')
    )
    #medical_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to='doctor_image/')
    specialty = models.CharField(max_length=255)
    patients = models.ManyToManyField(Patient, blank=True)

    def patient_count(self):
        return self.patients.count()

    def __str__(self):
        return self.name

class PatientHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    symptoms = models.TextField()

    def __str__(self):
        return f"History for {self.patient.name} on {self.appointment_date}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    is_reappointment = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment_date}"

class User(AbstractUser):
    email = models.EmailField(unique=True)
