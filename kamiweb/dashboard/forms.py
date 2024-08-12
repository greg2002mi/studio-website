from django import forms
from django.db.models import F
from blog.models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Videosam, Wedo, Forwhom
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

# SMM

class SmmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        # Make the query here
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('SMM service in Russian')
        self.fields['en'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['en'].widget.attrs['placeholder'] = _('SMM service in English')
        

    
    class Meta:
        model = SMM
        fields = ('title', 'en',)
        labels = {
            'title': _('In Russian'),
            'en': _('In English'),
        }

class EgSmmForm(forms.ModelForm):
    # published = forms.ChoiceField(choices=PUBLISHED_CHOICES, required=False, widget=forms.RadioSelect, label=_('Publish'))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        # Make the query here
        self.fields['title1'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title1'].widget.attrs['placeholder'] = _('Before')
        self.fields['short1'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['short1'].widget.attrs['placeholder'] = _('Description prior to...')
        self.fields['url1'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['url1'].widget.attrs['placeholder'] = _('(Can be blank) Link without https://...')
        self.fields['title2'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title2'].widget.attrs['placeholder'] = _('After')
        self.fields['short2'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['short2'].widget.attrs['placeholder'] = _('Description after...')
        self.fields['url2'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['url2'].widget.attrs['placeholder'] = _('(Can be blank) Link without https://...')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    
    class Meta:
        model = EgSMM
        fields = ('title1', 'short1', 'image1', 'url1',  'title2', 'short2', 'image2', 'url2', 'published', 'lang')
        labels = {
            'title1': _('Title of BEFORE example'),
            'short1': _('Description of BEFORE example'),
            'url1': _('URL before'),
            'title2': _('Title of RESULTS example'),
            'short2': _('Description of RESULTS example'),
            'url2': _('URL after'),
            'published': _('Publish'),
            'lang': _('By default its for russian'),
        }
        
# Services

class ServiceForm(forms.ModelForm):
    published = forms.ChoiceField(choices=PUBLISHED_CHOICES, required=False, widget=forms.RadioSelect, label=_('Publish'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        # Make the query here
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of service')
        self.fields['content'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['content'].widget.attrs['placeholder'] = _('Short description')
        self.fields['price'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['price'].widget.attrs['placeholder'] = _('Price')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    
    class Meta:
        model = Service
        fields = ('title', 'content', 'price', 'currency', 'published', 'lang',)
        labels = {
            'title': _('Title'),
            'content': _('Content'), 
            'price': _('Price'),  
            'currency': _('Currency'),
            'published': _('Publish'), 
            'lang': _('Language'),
            
        }
        
# CLients form
class ClientForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of Graphic design')
        self.fields['url'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['url'].widget.attrs['placeholder'] = _('website url. omit https://')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    class Meta:
        model = Client
        fields = ['title', 'url', 'image', 'published']
        labels = {
            'title': _('Title'),
            'url': _('Website link'),
            'image': _('Image'),
            'published': _('Publish'),
        }
        
# About us form
class AboutusForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['title'].widget.attrs['placeholder'] = _('Title of a post')
        self.fields['content'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['content'].widget.attrs['placeholder'] = _('Content')
        self.fields['published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    class Meta:
        model = Aboutus
        fields = ['title', 'content', 'team', 'studio', 'lang', 'published']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'team': _('Team image'),
            'studio': _('Second image'),
            'lang': _('Language'),
            'published': _('Publish'),
        }

# Contact us | My page form
class ContactInfoForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['greeting'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['greeting'].widget.attrs['placeholder'] = _('Greeting')
        self.fields['content'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['content'].widget.attrs['placeholder'] = _('Content')

    class Meta:
        model = Contact
        fields = ['greeting', 'image', 'content', 'lang']
        labels = {
            'greeting': _('Greeting'),
            'content': _('Content'),
            'image': _('Image'),
            'lang': _('Language'),
        }


class VideosamForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = Videosam
        fields = ['video1', 'video2', 'video3'] 
        labels = {
            'video1': _('Main video big'),
            'video2': _('small video 2'),
            'video3': _('small video 3'),
        }
        
class WedoForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['service'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['service'].widget.attrs['placeholder'] = _('Services we provide')
        self.fields['en'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['en'].widget.attrs['placeholder'] = _('Services we provide in English')
        self.fields['ko'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['ko'].widget.attrs['placeholder'] = _('Services we provide in Korean')
        

    class Meta:
        model = Wedo
        fields = ['service', 'en', 'ko' ]
        labels = {
            'service': _('Service'),
            'en': _('In English'),
            'ko': _('In Korean'),
            
        }

class ForwhomForm(forms.ModelForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['service'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['service'].widget.attrs['placeholder'] = _('What we achieve')
        self.fields['en'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['en'].widget.attrs['placeholder'] = _('What we achieve in English')
        self.fields['ko'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['ko'].widget.attrs['placeholder'] = _('What we achieve in Korean')
        

    class Meta:
        model = Forwhom
        fields = ['service', 'en', 'ko']
        labels = {
            'service': _('Service'),
            'en': _('In English'),
            'ko': _('In Korean'),
            
        }





        