from django.forms import ModelForm
from .models import VehicleDetail

class vehicleForm(ModelForm):
    class Meta:
        model = VehicleDetail
        fields = ['customer_name', 'customer_no', 'car_model', 'car_reg_no']