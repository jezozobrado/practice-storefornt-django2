from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    billing_street = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=255)
    billing_postal_code = models.PositiveIntegerField(null=True)
    shipping_street = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_postal_code = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.username
