from django.urls import path
from donatory import views

app_name = 'donatroy'

urlpatterns = [
    path('', views.donatory_home, name='home'),
    path('form/', views.blood_form, name='blood-form'),
    path('form/edit/<int:id>/', views.donor_blood_form_edit, name='blood-form-edit'),
    path('form/delete/<int:id>/', views.donor_blood_form_delete, name='blood-form-delete'),



]
