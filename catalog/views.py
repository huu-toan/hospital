from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from catalog.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from catalog.models import Patient
from catalog.models import Doctor
from catalog.models import PatientHistory
from catalog.models import Appointment
from django.db.models import Count
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .forms import PatientForm

# Create your views here.
def index(request):
    return render(request, 'card/card.html/', {})

def pro(request):
    doctor = Doctor.objects.all().order_by('-name')
    return render(request, 'hos_page/pro.html/', {'doctor': doctor})

def for_patient(request):
    return render(request, 'hos_page/for_patient.html/', {})

def introduce(request):
    return render(request, 'hos_page/introduce.html/', {})

def doctors(request):
    doctor = Doctor.objects.all().order_by('-name')
    return render(request, 'hos_page/pro.html', {'doctor': doctor})

def patient_form(request):
 
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PatientForm()
    return render(request, 'hos_page/patient_form.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')

def search(request):
    query = request.GET.get("query")
    qs = Doctor.objects.filter(name__icontains=query)
    return render(request, 'hos_page/search.html', {"doctors": qs})

def doctorinfo(request, id):
    doctor = Doctor.objects.get(pk = id)
    return render(request, 'hos_page/doctorinfo.html', {'doctor': doctor})

def doctorimage(request, id):
    doctor = Doctor.objects.get(pk = id)
    return render(request, 'hos_page/doctorimage.html', {'doctor': doctor})

def count_patients(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    patient_count = Patient.objects.filter(doctor=doctor).count()
    Doctor.save()
    return render(request, 'hos_page/patient_count.html', {'doctor': doctor, 'patient_count': patient_count})
