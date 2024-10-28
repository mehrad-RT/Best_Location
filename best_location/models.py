from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass

class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=2, related_name="userInformation")
    district_number = models.IntegerField()
    size = models.FloatField()
    product_grade = models.IntegerField()
    parking_place = models.IntegerField()
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Information for {self.user.username}"
