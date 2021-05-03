from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    profile = Aboutme.objects.all()
    skills = Skills.objects.all()
    experience = Experience.objects.all()
    refference = Refference.objects.all()
    portfolio = Portfolio.objects.all()
    education = Education.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact.objects.create( name = name, email = email, message = message)
        context = {'profile':profile,'skills':skills, 'experience':experience, 'refference':refference,'portfolio':portfolio, 'education':education,'contact':contact}
        return render(request, 'home.html',context)
        
    else:
        profile = Aboutme.objects.all()
        skills = Skills.objects.all()
        experience = Experience.objects.all()
        refference = Refference.objects.all()
        portfolio = Portfolio.objects.all()
        education = Education.objects.all()
        context = {'profile':profile,'skills':skills, 'experience':experience, 'refference':refference,'portfolio':portfolio, 'education':education}
        return render(request, 'home.html',context)

