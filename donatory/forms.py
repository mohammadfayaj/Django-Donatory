from PIL import Image
from django import forms
from django.core.files import File
from donatory.models import DonorInformation
from intl_tel_input.widgets import IntlTelInputWidget
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class DonorInformationForm(forms.ModelForm):
    class Meta:
        model = DonorInformation
        fields = ('name', 'phone_number', 'blood_group', 'current_address', 'permanent_address','profile_picture')
        widgets = {
            'phone_number' : PhoneNumberPrefixWidget(attrs=
                {'placeholder': (u'Phone Number'), 'id':'tel', 'class': "form-control", 'label':(u'Cellphone number')}),
        }