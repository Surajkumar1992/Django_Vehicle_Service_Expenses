from django.forms import ModelForm
from django import forms
from .models import VehicleDetail

class vehicleForm(ModelForm):
    class Meta:
        model = VehicleDetail
        fields = ['customer_name', 'customer_no', 'car_model', 'car_reg_no']

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_no': forms.TextInput(attrs={'class': 'form-control'}),
            'car_model': forms.TextInput(attrs={'class': 'form-control'}),
            'car_reg_no': forms.TextInput(attrs={'class': 'form-control'}),
        }