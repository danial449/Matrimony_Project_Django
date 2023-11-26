from typing import Any
from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import profile



class NewProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = "__all__"
        # fields = ["name" , 'age' .....] // this for specific field to put
        # exclude = ["name" , 'age' .....]  // mean exclude this fields from form but others all are shown

    is_married = forms.BooleanField(
        label="Status",  # Change the label here
        required=False  # Add other attributes as needed
    )   




def my_email_validator(email):
    if email.split('@')[1].split('.')[0].lower()=='hotmail':
        raise ValidationError("Email not accepatable")

class contactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(validators=[EmailValidator() , my_email_validator])
    verify_email = forms.CharField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)   
    
    def clean(self):
        cleaned_data= super().clean()

        name = cleaned_data.get('name')
        email = cleaned_data.get('email').lower()
        verify_email = cleaned_data.get('verify_email').lower()
        message = cleaned_data.get('message')

        cleaned_data['email'] = email
        cleaned_data['verify_email'] = verify_email

        if email != verify_email:
            raise ValidationError("Email Mismatch")
        return cleaned_data

class ProfileSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
