from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ClientRegistrationForm, VehicleForm
from .models import ClientRegistration, Vehicle

def clientregistration(request):
    form = ClientRegistrationForm()
    if request.method == "POST":
        formdata = ClientRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Client Registered Successfully"
            return render(request, "clientreg.html", {"clientform": form,"msg":msg})
        else:
            msg = "Failed to Register Client"
            return render(request, "clientreg.html", {"clientform": form, "msg": msg})
    return render(request,"clientreg.html",{"clientform":form})

def clientlogin(request):
    return render(request,"clientlogin.html")

def checkclientlogin(request):
    uname = request.POST["cusername"]
    pwd = request.POST["cpassword"]

    flag = ClientRegistration.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        cli = ClientRegistration.objects.get(username=uname)
        print(cli)
        request.session["cname"] = cli.clientname
        return render(request, "clienthome.html", {"cname": cli.clientname})
    else:
        msg = "Login Failed"
        return render(request, "clientlogin.html", {"msg": msg})

def clienthome(request):

    return render(request,"clienthome.html",)

def clientlogout(request):
    return render(request,"clientlogin.html")

def addvehicle(request):
    form = VehicleForm()
    if request.method == "POST":
        formdata = VehicleForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Vehicle Added Successfully"
            return render(request, "addvehicle.html", {"vehicleform": form,"msg":msg})
        else:
            msg = "Failed to Add Vehicle"
            return render(request, "addvehicle.html", {"vehicleform": form, "msg": msg})
    return render(request,"addvehicle.html",{"vehicleform":form})

def viewallvehicles(request):
    vehiclelist = Vehicle.objects.all()
    count = Vehicle.objects.count()
    return render(request, "viewallvehicles.html", { "vehiclelist": vehiclelist, "count": count})

def clientprofile(request):
    cname=request.session["cname"]
    ClientRegistration.objects.get(username=cname)
    return render(request,"clienthome.html",{"cname":cname})

def viewavehicle(request):

    vehiclelist = Vehicle.objects.all()
    return render(request,"viewavehicle.html",{"vehiclelist":vehiclelist})

def displayvehicle(request):
    pname = request.POST["pname"]
    vehiclelist = Vehicle.objects.filter(name__icontains=pname)
    return render(request,"displayvehicle.html",{"vehiclelist":vehiclelist})

def payment(request):
    value=2500
    return render(request,"finalpayment.html",{"value":value})

def pay(request):
    return render(request,"pay.html")
