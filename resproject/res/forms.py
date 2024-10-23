from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput()}    # additional features of the fields
        labels = {"Contact":"Provide Contact No"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form
