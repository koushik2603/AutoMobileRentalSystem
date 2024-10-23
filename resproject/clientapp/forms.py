from django import forms

from .models import ClientRegistration, Vehicle

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClientRegistration
        fields = "__all__"
        widgets = {"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}
        labels = {"clientname": "Manager Name","companyname":"Company Name"}

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
        labels = {"category":"Select Category","price":"Price(per Hour)"}