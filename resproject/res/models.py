from django.db import models

# Create your models here.
class Registration(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    contact = models.BigIntegerField(blank=False)
    location = models.CharField(max_length=100, blank=False)
    registrationtime = models.DateTimeField(blank=False, auto_now=True)

    class Meta:
        db_table = "registration_table"

