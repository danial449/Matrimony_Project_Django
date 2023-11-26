from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class Religion(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
       return self.name
   
class Sect(models.Model):
   name = models.CharField(max_length=100)
   religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='sects')

   def __str__(self):
       return self.name

class Caste(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
       return self.name

class Hobby(models.Model):
   name = models.CharField(max_length=100)

   class Meta:
    verbose_name_plural = 'Hobbies'
   def __str__(self):
       return self.name 

class FatherProfile(models.Model):
   name = models.CharField(max_length=100)
   occupation = models.CharField(max_length=100 , null=True , blank=True)

   def __str__(self):
       return self.name
   
class profile(models.Model):
    GENDER_CHOICE = [
        ('Male' , 'M'),
        ('Female' , 'F')
    ]
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile_pics/',null=True , blank=True)
    gender = models.CharField(max_length=10 , choices=GENDER_CHOICE)
    occupation = models.CharField(max_length=100 , null=True , blank=True)
    birth_date = models.DateField(null=True)
    is_married = models.BooleanField(default=False)
    email = models.EmailField(null=True , unique=True)

    religion = models.ForeignKey(Religion, on_delete=models.CASCADE  , related_name='profiles' , blank=True,null=True)
    sects = models.ForeignKey(Sect, on_delete=models.CASCADE ,  related_name='Followers' , blank=True, null=True)
    caste = models.ForeignKey(Caste, on_delete=models.CASCADE , related_name='profiles' , blank=True, null=True)
    hobbies = models.ManyToManyField(Hobby , related_name='profiles' , blank=True)
    father = models.OneToOneField(FatherProfile , on_delete=models.CASCADE , related_name='dependent' , blank=True, null=True)

    def save(self, *args, **kwargs):
       print(f'data updated for {self.name}')
       super().save(*args, **kwargs) # Call the real save() method

    def __str__(self):
      return self.name

