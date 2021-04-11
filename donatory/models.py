from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from intl_tel_input.widgets import IntlTelInputWidget
from django.utils import timezone

BLOOD_GROUP = [

    ('A+' , 'A+'),
    ('B+' , 'B+'),
    ('O+' , 'O+'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('A-' , 'A-'),
    ('B-' , 'B-'),
    ('O-' , 'O-')
]

class DonorInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length= 40, null=True, help_text='Enter Your Full Name')
    profile_picture = models.ImageField(upload_to='donor_pic', null=True, blank=True)
    phone_number = PhoneNumberField(help_text='Please Enter Your Valid Phone Number.',)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP, null=True,)
    current_address = models.CharField(max_length=50, null=True, help_text='Your devision and your city')
    permanent_address = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)



