from django import forms
from django.db.models import F
from .models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Call, Order
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
import os
from django.conf import settings
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput



PUBLISHED_CHOICES = [
    (True, _('Yes')),
    (False, _('No')),
]
# - Header all the titles, and backgrounds

class HeaderForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
        self.fields['title'].widget.attrs.update({
            'style': 'min-width: 100%',
            'placeholder': _('Enter header title')
        })
        self.fields['short'].widget.attrs.update({
            'style': 'min-width: 100%',
            'placeholder': _('Enter short description')
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file'
        })
        self.fields['page'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['height'].widget.attrs.update({
            'style': 'min-width: 100%',
            'placeholder': _('Enter height in pixels (optional)')
        })
        self.fields['top'].widget.attrs.update({
            'style': 'min-width: 100%',
            'placeholder': _('Enter top offset in pixels (optional)')
        })

    class Meta:
        model = Header
        fields = ['title', 'short', 'image', 'page', 'height', 'top']
        labels = {
            'title': _('Title'),
            'short': _('Short Description'),
            'image': _('Image'),
            'page': _('Page'),
            'height': _('Height (in pixels)'),
            'top': _('Top Offset (in pixels)'),
        }

# gfx
class GfxForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of Graphic design')
        self.fields['short'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['short'].widget.attrs['placeholder'] = _('Short description of Graphic design')
        self.fields['magn'].widget.attrs.update({
            'style': 'min-width: 80%',
            'placeholder': _('Magnification of image. Default = 3, 6 will take a half of row')
        })
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    class Meta:
        model = Gfx
        fields = ['title', 'short', 'image', 'published', 'magn' ]
        labels = {
            'title': _('Title'),
            'short': _('Short Description'),
            'image': _('Image'),
            'published': _('Publish'),
            'magn': _('Magnification'),
        }

# - video cases
class AddVidcatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of Video category in Russian')
        self.fields['en'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['en'].widget.attrs['placeholder'] = _('Title of Video category in English')
        
        
    class Meta:
        model = VidCat
        fields = ['title', 'en' ] 
        labels = {
            'title': _('In Russian'),
            'en': _('In English'),
        }

class AddYoutubeForm(forms.ModelForm):
    published = forms.ChoiceField(choices=PUBLISHED_CHOICES, required=False, widget=forms.RadioSelect, label=_('Publish'))
    # category = forms.ModelMultipleChoiceField(
    #     queryset=VidCat.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple, 
    #     label=_('Category')
    # )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of a Video Case')
        self.fields['short'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['short'].widget.attrs['placeholder'] = _('Short description of video')
        self.fields['url'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['url'].widget.attrs['placeholder'] = _('Paste "embed" url link, taken from desired youtube clip')
        self.fields['produced'].widget.attrs['class'] = 'datetimepicker'
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['category'].widget.attrs['class'] = 'form-control2'
        self.fields['category'] = forms.ChoiceField(
            choices=[(cat.id, cat.title) for cat in VidCat.objects.all()],
            required=True,
            widget=forms.RadioSelect,
            label=_('Category')
            )
        
    class Meta:
        model = Vid
        fields = ['title', 'short', 'url', 'published', 'category', 'produced', ] 
        widgets = {
            "produced": DateTimePickerInput(),
        }
        labels = {
            'title': _('Title'),
            'short': _('Short description'),
            'url': _('Short description'),
            'published': _('Publish'),
            'category': _('Category'),
            #'category': _('Short description'),
            'produced': _('Production date'),
        }

# - Reels
class AddReelcatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of Video category in Russian')
        self.fields['en'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['en'].widget.attrs['placeholder'] = _('Title of Video category in English')
        
        
    class Meta:
        model = ReelCat
        fields = ['title', 'en' ] 
        labels = {
            'title': _('In Russian'),
            'en': _('In English'),
        }


class AddReelForm(forms.ModelForm):
    
    published = forms.ChoiceField(choices=PUBLISHED_CHOICES, required=False, widget=forms.RadioSelect, label=_('Publish'))

   # in case of ManytoMany relations
    # category = forms.ModelMultipleChoiceField(
    #     queryset=ReelCat.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple, 
    #     label=_('Category')
    # )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of a Video Case')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['category'].widget.attrs['class'] = 'form-control2'
        self.fields['category'] = forms.ChoiceField(
            choices=[(cat.id, cat.title) for cat in ReelCat.objects.all()],
            required=True,
            widget=forms.RadioSelect,
            label=_('Category')
        )    
        
    class Meta:
        model = Reel
        fields = ['title', 'video', 'category', 'published'] 
        labels = {
            'title': _('Title'),
            'video': _('Your reel video'),
            'category': _('Category'),
            'published': _('Publish'),
        }


# - Photography
class AddImgcatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of Video category in Russian')
        self.fields['en'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['en'].widget.attrs['placeholder'] = _('Title of Video category in English')
        
        
    class Meta:
        model = ImgCat
        fields = ['title', 'en' ] 
        labels = {
            'title': _('In Russian'),
            'en': _('In English'),
        }


class AddImageForm(forms.ModelForm):
    published = forms.ChoiceField(choices=PUBLISHED_CHOICES, required=False, widget=forms.RadioSelect, label=_('Publish'))
    # category = forms.ModelMultipleChoiceField(
    #     queryset=ImgCat.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple, 
    #     label=_('Category')
    # )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of a Video Case')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['category'].widget.attrs['class'] = 'form-control2'
        self.fields['category'] = forms.ChoiceField(
            choices=[(cat.id, cat.title) for cat in ImgCat.objects.all()],
            required=True,
            widget=forms.RadioSelect,
            label=_('Category')
        )    
        
    class Meta:
        model = Image
        fields = ['title', 'image', 'category', 'published'] 
        labels = {
            'title': _('Title'),
            'image': _('Image'),
            'category': _('Category'),
            'published': _('Publish'),
        }

# Websites
class AddWebsiteForm(forms.ModelForm):
    published = forms.ChoiceField(choices=PUBLISHED_CHOICES, required=False, widget=forms.RadioSelect, label=_('Publish'))
    # category = forms.ModelMultipleChoiceField(
    #     queryset=ImgCat.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple, 
    #     label=_('Category')
    # )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Customer or Company name')
        self.fields['url'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['url'].widget.attrs['placeholder'] = _('Website address must start from www...')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        
    class Meta:
        model = Website
        fields = ['title', 'url', 'image', 'published'] 
        labels = {
            'title': _('Title'),
            'url': _('URL'),
            'image': _('Image'),
            'published': _('Publish'),
        }