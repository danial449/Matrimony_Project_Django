from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path("login/", LoginView, name="login"),
    path("register/", RegisterView, name="register"),
    path("logout/", LogoutView, name="logout"),
    path("delete/", DeleteAccountView, name="delete_account"),
    path("verify_email/<str:token>/", verify_email_view, name="verify_email"),
]

