from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def nannies(request):

    return render(request,'nannies.html')

def pricing(request):

    return render(request,'pricing.html')

def services(request):

    return render(request,'services.html')

def testimonial(request):

    return render(request,'testimonial.html')
