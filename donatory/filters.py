from . models import *
import django_filters
from django import forms
from django_filters.filters import RangeFilter,DateFilter,CharFilter
from django_filters.widgets import RangeWidget,CSVWidget,DateRangeWidget,SuffixedMultiWidget
from django.forms import CheckboxSelectMultiple,RadioSelect


# Creating product filters
class DonorInformationFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search Donor...' , 'class':'form-control '}), label=False)
	current_address = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search by donor lucations...' , 'class':'form-control '}), label='Filter By Donor Current Address')
	blood_group = django_filters.filters.ChoiceFilter(choices=BLOOD_GROUP,widget=forms.Select(attrs={'class': 'custom-select form-control'},))

	class Meta:
		model = DonorInformation
		fields = ['name','current_address','blood_group',]



























