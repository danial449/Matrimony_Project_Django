from django.contrib import admin
from .models import *
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display = ( 'id' , 'name' , 'age' , 'profile_pic' , 'gender' , 'occupation' , 'birth_date' , 'is_married' , 'email')

    list_display_links = ('name' , 'age' , 'profile_pic' , 'gender' , 'occupation' , 'birth_date' , 'is_married' , 'email')
    
    list_filter = ('gender' , 'is_married')

    search_fields =('occupation',)

admin.site.register(profile , profileAdmin)




class ReligionAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'get_profile')

    def get_profile(self , obj):
       profiles = ", ".join([profile.name for profile in obj.profiles.all()])  
       return profiles
    get_profile.short_description = "Profiles"


admin.site.register(Religion , ReligionAdmin)




class SectAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'religion' , 'get_profile')

    def get_profile(self , obj):
       sect = ", ".join([profile.name for profile in obj.Followers.all()])  
       return sect
    get_profile.short_description = "Profiles"


admin.site.register(Sect , SectAdmin)



class CasteAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'get_profile')

    def get_profile(self , obj):
       caste = ", ".join([profile.name for profile in obj.profiles.all()])  
       return caste
    get_profile.short_description = "Profiles"

admin.site.register(Caste , CasteAdmin)




class HobbyAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'get_profile')

    def get_profile(self , obj):
       profiles = ", ".join([profile.name for profile in obj.profiles.all()])  
       return profiles
    get_profile.short_description = "Followers"

admin.site.register(Hobby , HobbyAdmin)




class FatherProfileAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'occupation' , 'dependent')

admin.site.register(FatherProfile , FatherProfileAdmin)

# class ContactFormAdmin(admin.ModelAdmin):
#     list_display = ('name' , 'email' , 'message')
# admin.site.register(ContactForm , ContactFormAdmin)

