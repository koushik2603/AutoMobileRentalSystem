from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

from .forms import RegistrationForm
from .models import Registration
from clientapp.models import Vehicle



def homepage(request):
    return render(request,"index.html")

def loginpage(request):
    return render(request,"login.html")

def checkuserlogin(request):
    uname=request.POST["username"]
    pwd=request.POST["pswd"]

    flag=Registration.objects.filter(Q(username=uname) & Q(password=pwd))
    print(flag)

    if flag:
        user=Registration.objects.get(username=uname)
        print(user)
        print(user.fullname) #other fields also
        request.session["uname"]=user.username
        return render(request,"loginsuc.html",{"uname":user.username})
    else:
        msg="Login Failed"
        return render(request,"login.html",{"msg":msg})

def loginsuccesspage(request):
    return render(request,"loginsuc.html")


def contactuspage(request):
    return render(request,"contactus.html")

def checkoutpage(request):
    return render(request,"checkout.html")

def subscribepage(request):
    return render(request,"subscribe.html")


def signuppage3(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"reg.html",{"msg":msg})
        else:
            msg="Registraion Failed. Username/email already exists"
            return render(request, "reg.html", {"msg": msg,'form':form})
    return render(request,"reg.html",{"form":form})


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

def loginhome(request):
    return render(request,"loginhome.html")

def reghome(request):
    return render(request,"reghome.html")

"""def viewvehicles(request):
    return render(request,"renterviewallvehicles.html")"""