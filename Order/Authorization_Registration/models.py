from django.db import models
# 
# Create your models here.
class Registration(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField()
