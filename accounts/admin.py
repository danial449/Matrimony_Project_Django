from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('id' , 'username' , 'email',)
    search_fields = ('username' , 'email',)

    fieldsets = UserAdmin.fieldsets + (  # Include 'gender' in the 'Personal Information' section
        ('Other Information', {
            'fields': ('gender',
                       'is_email_verified',
                       'email_verification_token',),
        }),
    )
admin.site.register(CustomUser , CustomUserAdmin)