from django.db import models
from django.utils import timezone
from datetime import datetime
from users.models import CustomUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import FileExtensionValidator 
import random

STATUS = (
    (0,_("Applied")),
    (1,_("Processing")),
    (2,_("Closed"))
)

CALL = (
    (0,_("New")),
    (1,_("Called")),
    (2,_("Waiting for responce")),
    (3, _("Closed"))
)

CURRENCY = (
    (0,_("---")),
    (1,_("KRW")),
    (2,_("USD")),
    (3, _("RUB"))
)

RANK = (
    (0,_("---")),
    (1,_("Very unpleasant")),
    (2,_("Unpleasant")),
    (3,_("OK")),
    (4,_("Good")),
    (5,_("Excellent"))
)

LANG = (
    (0,_("No lang")),
    (1,_("English")),
    (2,_("Russian")),
    # (3, _("Korean"))
)

PAGE = (
    (0,_("None")),
    (1,_("Home")),
    (2,_("Video case")),
    (3,_("Reel")),
    (4,_("Photography")),
    (5,_("Grachic Design")),
    (6,_("Website")),
    (7,_("SMM")),
    (8,_("Services")),
    (9,_("About Studio")),
    (10,_("Clients")),
    (11,_("Reviews")),
    (12,_("Contacts")),
    (13,_("Make an order")),
    (14,_("Call me")),
    (20,_("Order")),
    (21,_("Write")),
    (98,_("Success page")),
    (99,_("Failed page")),
    (100,_("Without title  (200) (-300)")),

)


# general info, phone number, address etc. -----------------------------------------------------------------

    

class Global(models.Model):
    address = CKEditor5Field(_('Address'), config_name='extends', blank=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=False, blank=True, null=True)
    navermap = models.CharField(max_length=255, blank=True, null=True)
    naver_clientid = models.CharField(max_length=255, blank=True, null=True)
    naver_clientkey = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # schedule_weekday = models.CharField(max_length=255) # something like 
    # schedule_start = models.CharField(max_length=255)
    # schedule_end = models.CharField(max_length=255)
    # schedule_lunch = models.CharField(max_length=255)


# gallery -----------------------------------------------------------------
def generate_filename(instance, filename):
    current_datetime = datetime.now()
    filename = f"img/{current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}_{filename}"
    return filename

# def generate_random_width():
#     return random.randint(350, 450)

class ImgCat(models.Model):
    title = models.CharField(max_length=255)
    en = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=generate_filename)
    # category = models.ManyToManyField(ImgCat, blank=True, related_name='image')
    category = models.ForeignKey(ImgCat, on_delete=models.CASCADE, blank=True, related_name='image')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    # fade = models.IntegerField(blank=True, null=True)
    # width = models.IntegerField(default=generate_random_width)
    
    # class Meta:
    #     ordering=['-date']
    
    # def save(self, *args, **kwargs):
    #     if not self.width:
    #         self.width = generate_random_width()
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title)
    
    def delete(self, *args, **kwargs):
        self.imgae.delete()  # Delete the associated file
        super().delete(*args, **kwargs)  # Call the superclass delete method

# Header -----------------------------------------------------------------

# def generate_filename(instance, filename):
#     current_datetime = datetime.now()
#     filename = f"header/{current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}_{filename}"
#     return filename



class Header(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    short = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=generate_filename)
    page = models.IntegerField(choices=PAGE, default=0)
    height = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    
 # video cases -----------------------------------------------------------------   
class VidCat(models.Model):
    title = models.CharField(max_length=255)
    en = models.CharField(max_length=255)
    # image = image = models.ImageField(default='servicecat.gif', upload_to=generate_filename)
    
    def __str__(self):
        return self.title

class Vid(models.Model):
    title = models.CharField(max_length=255)
    short = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField()
    # image = models.ImageField(upload_to="img", blank=True, null=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    published = models.BooleanField(default=True)
    # category = models.ManyToManyField(VidCat, blank=True, related_name='video')
    category = models.ForeignKey(VidCat, on_delete=models.CASCADE, blank=True, related_name='video')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    produced = models.DateTimeField(null=True, blank=True)
    # content = CKEditor5Field(_('Content'), config_name='extends', blank=True)
    # updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)   


 # reels -----------------------------------------------------------------
class ReelCat(models.Model):
    title = models.CharField(max_length=255)
    en = models.CharField(max_length=255)
    # image = image = models.ImageField(default='servicecat.gif', upload_to=generate_filename)
    def __str__(self):
        return self.title

def generate_vidfilename(instance, filename):
    current_datetime = datetime.now()
    filename = f"video/{current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}_{filename}"
    return filename

class Reel(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to=generate_vidfilename, null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    # image = models.ImageField(upload_to="img", blank=True, null=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    published = models.BooleanField(default=True)
    # category = models.ManyToManyField(ReelCat, blank=True, related_name='reel')
    category = models.ForeignKey(ReelCat, on_delete=models.CASCADE, blank=True, related_name='reel')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # content = CKEditor5Field(_('Content'), config_name='extends', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)  

    def delete(self, *args, **kwargs):
        self.video.delete()  # Delete the associated file
        super().delete(*args, **kwargs)  # Call the superclass delete method

# graphic design -----------------------------------------------------------------
# class GfxCat(models.Model):
#     title = models.CharField(max_length=255)
    # image = image = models.ImageField(default='servicecat.gif', upload_to=generate_filename)
def generate_gfxfilename(instance, filename):
    current_datetime = datetime.now()
    filename = f"gfx/{current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}_{filename}"
    return filename


class Gfx(models.Model):
    title = models.CharField(max_length=150)
    short = models.CharField(max_length=150)
    image = models.ImageField(upload_to=generate_gfxfilename)
    published = models.BooleanField(default=True)
    # category = models.ForeignKey(GfxCat, on_delete=models.SET_NULL, null=True, blank=True, related_name='Gfx')
    date = models.DateTimeField(auto_now_add=True)
    magn = models.IntegerField(null=True, blank=True)
    # fade = models.IntegerField(blank=True, null=True)
    # width = models.IntegerField(default=generate_random_width)

    def delete(self, *args, **kwargs):
        self.image.delete()  # Delete the associated file
        super().delete(*args, **kwargs)  # Call the superclass delete method    
# services -----------------------------------------------------------------   

# class ServiceCat(models.Model):
    # title = models.CharField(max_length=255)
    # image = image = models.ImageField(default='servicecat.gif', upload_to=generate_filename)


class Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to="img", blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency = models.IntegerField(choices=CURRENCY, default=1)
    published = models.BooleanField(default=True)
    lang = models.IntegerField(choices=LANG, default=2)
    # category = models.ForeignKey(ServiceCat, on_delete=models.SET_NULL, null=True, blank=True, related_name='service')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)   

# websites ----------------------------------------------------------------- 
def generate_webfilename(instance, filename):
    current_datetime = datetime.now()
    filename = f"web/{current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}_{filename}"
    return filename

class Website(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_webfilename)
    published = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        self.image.delete()  # Delete the associated file
        super().delete(*args, **kwargs)  # Call the superclass delete method 
  
# SMM -----------------------------------------------------------------   
class SMM(models.Model):
    title = models.CharField(max_length=255)
    en = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
class EgSMM(models.Model):
    title1 = models.CharField(max_length=255)
    short1 = models.TextField()
    image1 = models.ImageField(upload_to=generate_filename)
    url1 = models.TextField(null=True, blank=True)
    title2 = models.CharField(max_length=255)
    short2 = models.TextField()
    image2 = models.ImageField(upload_to=generate_filename)
    url2 = models.TextField(null=True, blank=True)
    lang = models.IntegerField(choices=LANG, default=2)
    published = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


# about our studio -----------------------------------------------------------------   
class Aboutus(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    team = models.ImageField(upload_to=generate_filename, null=True, blank=True)
    studio = models.ImageField(upload_to=generate_filename, null=True, blank=True)
    lang = models.IntegerField(choices=LANG, default=2)
    published = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


# clients -----------------------------------------------------------------   
class Client(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_filename)
    published = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)



# reviews -----------------------------------------------------------------
class Review(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(choices=RANK, default=0)
   
# contact info -----------------------------------------------------------------  
class Contact(models.Model):
    greeting = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_filename)
    content = CKEditor5Field(_('Content'), config_name='extends', blank=True)
    lang = models.IntegerField(choices=LANG, default=2)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


# MAIN -----------------------------------------------------------------------
class Videosam(models.Model):
    video1 = models.FileField(upload_to=generate_vidfilename, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    video2 = models.FileField(upload_to=generate_vidfilename, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    video3 = models.FileField(upload_to=generate_vidfilename, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

class Wedo(models.Model):
    service = models.CharField(max_length=255)
    en = models.CharField(max_length=255, null=True, blank=True)
    ko = models.CharField(max_length=255, null=True, blank=True)
    

class Forwhom(models.Model):
    service = models.CharField(max_length=255)
    en = models.CharField(max_length=255, null=True, blank=True)
    ko = models.CharField(max_length=255, null=True, blank=True)
