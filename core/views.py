from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,'core/Home.html')

def branches(request):
    return render(request,'core/Branches.html')

def coaches(request):
    return render(request,'core/Coaches.html')

def classes(request):
    return render(request,'core/Classes.html')

def membership_plans(request):
    return render(request,'core/Membership_plans.html')

def contact(request):
    return render(request,'core/Contact.html')

def support_process(request):
    email = request.POST.get('txt_email')
    submitted_date = request.POST.get('txt_date')
    message = request.POST.get('txt_message')
    return HttpResponse(f'Email: {email}<br>Date: {submitted_date}<br>Message: {message}')