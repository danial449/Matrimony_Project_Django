from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def profileListView(request):
    profiles = profile.objects.all()
    user = request.user
    return render( request , 'profile_app/profile_list.html' , {'profiles' : profiles ,'user':user}) 

def profileDetailView(request , profile_id):
    Profile = profile.objects.get(id=profile_id)
    user = request.user
    return render( request , 'profile_app/profile_details.html', {'Profile' : Profile ,'user':user}) 

def profileDeleteView(request , profile_id):
    Profile_delete = profile.objects.get(id=profile_id)
    Profile_delete.delete()
    # profiles = profile.objects.all()
    return redirect(reverse('profile_app:profile_list'))
    # return render( request , 'profile_app/profile_list.html' , {'profiles' : profiles}) 
    
@login_required
def profileCreateView(request):
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to create a new profile
            return redirect(reverse('profile_app:profile_list'))
    else:
        form = NewProfileForm()
    return render(request, 'profile_app/form.html', {'form': form})





def ContactFormView(request):
    if request.method =='POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(f"NAME:{form.cleaned_data['name']}")
            print(f"EMAIL:{form.cleaned_data['email']}")
            print(f"MESSAGE:{form.cleaned_data['message']}")
    else:
        form = contactForm()    
    return render( request , 'profile_app/contactForm.html' , {'form':form}) 

def profileSearchView(request):
    search_query = request.GET.get('search_query', '')
    
    if search_query:
        profiles = profile.objects.filter(name__icontains=search_query)
        template_name = 'profile_app/profile_search_results.html'
    else:
        profiles = profile.objects.all()
        template_name = 'profile_app/profile_list.html'
    
    return render(request, template_name, {'profiles': profiles, 'search_query': search_query})





