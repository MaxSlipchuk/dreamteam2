from django.db import models

# Create your models here.
class ShoppingCart(models.Model):
    username = models.CharField(max_length=255)
    perfum_name = models.CharField(max_length=255)
    price = models.IntegerField()
    perfum_count = models.IntegerField()
    perfum_sum = models.IntegerField()