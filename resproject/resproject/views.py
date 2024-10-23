"""
from django.http import HttpResponse
from django.shortcuts import redirect, render


def homepage(request):
    return render(request,"index.html")

def loginpage(request):
    return render(request,"login.html")

def signuppage(request):
    return render(request,"signup.html")

def contactuspage(request):
    return render(request,"contactus.html")

def checkoutpage(request):
    return render(request,"checkout.html")

def subscribepage(request):
    return render(request,"subscribe.html")

def signuppage1(request):
    return render(request,"signup1.html")

def signuppage2(request):
    return render(request,"signup2.html")

def aboutpage(request):
    return render(request,"about.html")

def book0page(request):
    return render(request,"book0.html")

def aboutuspage(request):
    return render(request,"aboutus.html")

def carspage(request):
    return render(request,"cars.html")

def bikespage(request):
    return render(request,"bikes.html")

def truckspage(request):
    return render(request,"trucks.html")
"""