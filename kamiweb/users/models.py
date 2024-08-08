import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(_("email address"), unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    telephone = PhoneNumberField(blank=True, null=True) 
    phone = PhoneNumberField(blank=True, null=True) 
    birthday = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, blank=True) 
    avatar = models.ImageField(default='noface.png', upload_to='profile_images/')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def get_full_name(self):
        return reverse('last_name' + '' + 'first_name')





