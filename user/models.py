from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from base.models import Base_Model

# Create your models here.

class Profile(Base_Model, AbstractBaseUser):
    icon = models.ImageField(upload_to='icons/', null=True, blank=True, default="Rasm yuklanmagan")
    bio = models.TextField(null=True, blank=True, default="Ma'lumot kiritilmagan")
    phone_number = models.CharField()
    birth = models.DateField(null=True, blank=True, default="Ma'lumot kiritilmagan")

    def __str__(self):
        return self.user.username

