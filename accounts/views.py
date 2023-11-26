from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from .models import *
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , authenticate ,logout
from django.contrib import messages
from .forms import *
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = CustomeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False
            user.email_verification_token = str(uuid.uuid4())
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            activation_link = f'http://{current_site}/accounts/verify_email/{user.email_verification_token}/'
            message = f'click the link to activate your account:{activation_link}'
            email_from = 'danialrafique7@gmail.com'
            recipeient_list = [user.email]
            send_mail(subject, message, email_from, recipeient_list)
            return redirect('accounts:login')
    else:
        form = CustomeRegistrationForm()
    return render(request  , 'accounts/register.html', {'form':form , 'user': request.user})

def verify_email_view(request , token):
    try:
        user = CustomUser.objects.get(email_verification_token = token)
        if user:
           user.is_email_verified = True
           user.email_verification_token = None
           user.save()
           return redirect('accounts:login')
    except:
        return HttpResponse("Activation Link is Invalid")

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            if user.is_email_verified:
                login(request , user)
                return redirect('profile_app:profile_list')
            else:
                messages.error(request , 'Please verify your Email')
                return redirect('accounts:login')
    else:
        form = AuthenticationForm()
    return render(request , 'accounts/login.html' , {'form':form ,'user': request.user})

def LogoutView(request):
    logout (request)
    return redirect('profile_app:profile_list')

def DeleteAccountView(request):
    request.user.delete()
    messages.success(request,'Your account has been deleted successfully')
    return redirect('accounts:login')