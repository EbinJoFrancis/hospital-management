from django.shortcuts import render
from .models import doctorss,Apodoc

# Create your views here.
def Home(request):
   doctor=Apodoc.objects.all()[0:8]
   return render(request,'home.html',{'DOCTORSS':doctor})

def Home1(request):
   doctor=Apodoc.objects.all()[0:8]
   return render(request,'home1.html',{'DOCTORSS':doctor})

def Contact(request):
   return render(request,'contact.html')

def Department(request):
   return render(request,'department.html')

# def Doctor(request):
#    return render(request,'doctor.html')

def Doctor(request):
   doctor=Apodoc.objects.all()
   return render(request,'doctor.html',{'DOCTORS':doctor})

def Appoinment(request):
   return render(request,'appoinment.html')