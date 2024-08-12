from django import forms
from django.db.models import F
from .models import Review, Contact, Call, Order
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
import os
from django.conf import settings
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django_ckeditor_5.widgets import CKEditor5Widget



PUBLISHED_CHOICES = [
    (True, _('Yes')),
    (False, _('No')),
]
