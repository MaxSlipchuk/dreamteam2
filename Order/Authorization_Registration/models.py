from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField()



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=13, null=True, blank=True)

    @classmethod
    def create_user_profile(cls, username, password, first_name, last_name, telephone, email):
        # Спочатку створюємо користувача з використанням стандартної моделі User
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)

        # Потім створюємо UserProfile і пов'язуємо його з користувачем
        user_profile = cls(user=user, telephone=telephone)
        user_profile.save()

        return user_profile

    