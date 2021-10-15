from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VehicleDetail(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_no = models.IntegerField(null=False)
    car_model = models.CharField(max_length=50)
    car_reg_no = models.IntegerField()
    car_servicedate_started = models.DateTimeField(auto_now_add=True)
    car_servicedate_completed = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name, self.car_reg_no

