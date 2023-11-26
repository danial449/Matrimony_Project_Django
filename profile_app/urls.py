from django.urls import path
from .views import *

app_name = 'profile_app'

urlpatterns = [
    path('' , profileListView , name= 'profile_list'),
    path('<int:profile_id>' , profileDetailView , name= 'profile_detail'),
    path('<int:profile_id>/delete' , profileDeleteView , name= 'profile_delete'),
    path('create/' , profileCreateView , name= 'profile_create'),
    path('contact/' , ContactFormView, name= 'contactform'),
    path('search/', profileSearchView, name='profile_search'),

]