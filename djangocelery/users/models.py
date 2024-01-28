from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    car_choices = (
        ('mazda', "Mazda Axela"),
        ('toyota', "Toyota TX"),
        ('honda', "Honda CR-V")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=256, null=True)
    car = models.CharField(max_length=256, choices=car_choices, default='mazda')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'