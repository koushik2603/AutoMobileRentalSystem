from django.db import models
from django.core.validators import MaxValueValidator

class ClientRegistration(models.Model):
    companyname = models.CharField(max_length=100, blank=False)
    clientname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    contact = models.BigIntegerField(blank=False)
    location = models.CharField(max_length=100, blank=False)
    registrationtime = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.companyname

    class Meta:
        db_table = "client_registration_table"

class Vehicle(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("2-Wheeler", "2-Wheeler"), ("4-Wheeler", "4-Wheeler"), ("Trucks","Trucks"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=400,blank=False)
    price = models.PositiveIntegerField(blank=False)
    hours = models.IntegerField(blank=False,validators=[MaxValueValidator(48)],default=1)
    image = models.FileField(blank=False,upload_to="vehicleimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "vehicle_table"