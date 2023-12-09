from django.db import models

# Create your models here.
class ShoppingCart(models.Model):
    username = models.CharField(max_length=255)
    perfum_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    perfum_count = models.IntegerField(null=True, blank=True)
    perfum_sum = models.IntegerField(null=True, blank=True)