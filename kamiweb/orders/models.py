from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

STATUS = (
    (0,_("Applied")),
    (1,_("Processing")),
    (2,_("Closed"))
)

# make order -----------------------------------------------------------------
class Order(models.Model):
    name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(_("email address"), unique=False)
    # reservation = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField()  # here to add all the info of an order
    
    
# request a call -----------------------------------------------------------------   
class Call(models.Model):
    name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(_("email address"), unique=False, blank=True, null=True)
    # reservation = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    question1 = models.TextField(blank=True, null=True)
    question2 = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)