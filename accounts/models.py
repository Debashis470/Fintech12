from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    extra_password = models.CharField(max_length=128, blank=True, null=True)  # custom password field

    def __str__(self):
        return self.user.username
