from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', post_list , name='post_list'),
    path('post/<int:pk>/', post_details , name='post_details'),
    path('post/new/', new_post , name='new_post'),
    path('post/<int:pk>/edit/', post_edit , name='post_edit'),
    path('post/<int:pk>/delete/', post_delete , name='post_delete'),
    path('post/<int:pk>/comment/', add_comment , name='add_comment'),
]
