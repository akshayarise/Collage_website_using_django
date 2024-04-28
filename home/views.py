from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages




# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        disc = request.POST.get('disc')
        contact = Contact(name = name, email=email, phone=phone, disc=disc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def achivement(request):
    return render(request, 'achivement.html')

def admission(request):
    return render(request, 'admission.html')
    
def aicteapproval(request):
    return render(request, 'aicteapproval.html')

def affiliation(request):
    return render(request, 'affiliation.html')

def btech(request):
    return render(request, 'btech.html')

def chairmanmessage(request):
    return render(request, 'chairmanmessage.html')

def communicationlab(request):
    return render(request, 'communicationlab.html')

def computercenter(request):
    return render(request, 'computercenter.html')

def contectus(request):
    return render(request, 'contectus.html')

def directormessage(request):
    return render(request, 'directormessage.html')

def facility(request):
    return render(request, 'facility.html')

def fee(request):
    return render(request, 'fee.html')

def gausthouse(request):
    return render(request, 'gausthouse.html')

def hostals(request):
    return render(request, 'hostals.html')

def library(request):
    return render(request, 'library.html')

def orgenizationchar(request):
    return render(request, 'orgenizationchar.html')

def polytechnic(request):
    return render(request, 'polytechnic.html')

def program(request):
    return render(request, 'program.html')

def secreterymessage(request):
    return render(request, 'secreterymessage.html')

def sports(request):
    return render(request, 'sports.html')

def wifi(request):
    return render(request, 'wifi.html')

def department(request):
    return render(request, 'department.html')
def ash(request):
    return render(request, 'ash.html')
def cseit(request):
    return render(request, 'cseit.html')
def me(request):
    return render(request, 'me.html')
def ce(request):
    return render(request, 'ce.html')
def ece(request):
    return render(request, 'ece.html')
def eee(request):
    return render(request, 'eee.html')
def dp(request):
    return render(request, 'dp.html')
def careerideal(request):
    return render(request, 'careerideal.html')
def photogallery(request):
    return render(request, 'photogallery.html')
def lifeideal(request):
    return render(request, 'lifeideal.html')

