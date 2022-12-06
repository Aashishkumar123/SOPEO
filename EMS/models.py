from django.db import models
from django.db.models import AutoField
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class Userall(models.TextChoices):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    account_type = models.CharField(max_length=20,choices=Userall.choices,default='other',blank=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True, blank=True, default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self) :
        return self.name

class add(models.Model):
    department = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100,null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    priority = models.CharField(max_length=100, null=True, blank=True)
    mobile= models.CharField(max_length=100, null=True, blank=True)
    # Description= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return self.name
    
class Admin(models.Model):
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
