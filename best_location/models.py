from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=2 , related_name="userInformation")
    district_number = models.FloatField()
    size = models.FloatField()
    product_grade = models.FloatField()
    parking_place = models.FloatField()
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.district_number)
