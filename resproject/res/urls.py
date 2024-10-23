
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("login", views.loginpage, name="login"),
    path("logout", views.loginpage, name="logout"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("loginsuccess", views.loginsuccesspage, name="loginsuccess"),
    path("registrationsuccess", views.loginpage, name="registrationsuccess"),
    path("contactus", views.contactuspage, name="contactus"),
    path("checkout", views.checkoutpage, name="checkout"),
    path("subscribe", views.subscribepage, name="subscribe"),
    path("about", views.aboutpage, name="about"),
    path("book0", views.book0page, name="book0"),
    path("aboutus", views.aboutuspage, name="aboutus"),
    path("cars", views.carspage, name="cars"),
    path("bikes", views.bikespage, name="bikes"),
    path("trucks", views.truckspage, name="trucks"),
    path("signup3", views.signuppage3, name="signup3"),
    path("loginhome", views.loginhome, name="loginhome"),
    path("reghome", views.reghome, name="reghome"),
    #path("viewvehicles", views.viewvehicles, name="viewvehicles"),

]