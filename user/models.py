from django.db import models
from django.contrib.auth.models import User, AbstractUser
from base.models import Base_Model

# Create your models here.

class Profile(Base_Model, AbstractUser):
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField()
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

