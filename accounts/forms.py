from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class CustomeRegistrationForm(UserCreationForm):
    gender = forms.ChoiceField(choices =CustomUser.GENDER_CHOICES , widget=forms.RadioSelect)
    class Meta:
        model = CustomUser
        fields = ['username' , 'email','gender','password1' , 'password2']