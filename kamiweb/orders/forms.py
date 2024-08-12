from django import forms
from .models import Order, Call
from blog.models import Review
from django.utils.translation import gettext as _

class OrderForm(forms.ModelForm):
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'common-input mb-20 form-control'
        
        self.fields['name'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['name'].widget.attrs['placeholder'] = _('Leave us your name')
        self.fields['email'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['email'].widget.attrs['placeholder'] = _('Your email to contact you')
        self.fields['phone'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['phone'].widget.attrs['placeholder'] = _('Your phone number')
        

    class Meta:
        model = Order
        fields = ['name', 'phone', 'email' ]
        labels = {
            'name': _('Full Name'),
            'phone': _('Phone Number'),
            'email': _('Email Address'),
        }

class CallmeForm(forms.ModelForm):
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'common-input mb-20 form-control'
        
        self.fields['name'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['name'].widget.attrs['placeholder'] = _('Leave us your name')
        self.fields['email'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['email'].widget.attrs['placeholder'] = _('Your email to contact you')
        self.fields['phone'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['phone'].widget.attrs['placeholder'] = _('Your phone number')
        self.fields['question1'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['question1'].widget.attrs['placeholder'] = _('What service are you interested in?')
        self.fields['question2'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['question2'].widget.attrs['placeholder'] = _('What time is convenient for you to receive a call?')
        self.fields['note'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['note'].widget.attrs['placeholder'] = _('Any questions? Or anything you would like to add?')
        

    class Meta:
        model = Call
        fields = ['name', 'phone', 'email', 'question1', 'question2', 'note', ]
        labels = {
            'name': _('Full Name'),
            'phone': _('Phone Number'),
            'email': _('Email Address'),
            'question1': _('Q1'),
            'question2': _('Q2'),
            'note': _('Note'),
        }
        
        
class WriteForm(forms.ModelForm):
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'common-input mb-20 form-control'
        
        self.fields['name'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['name'].widget.attrs['placeholder'] = _('Leave us your name')
        self.fields['role'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['role'].widget.attrs['placeholder'] = _('Your role or position')
        self.fields['company'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['company'].widget.attrs['placeholder'] = _('Your workplace')
        self.fields['content'].widget.attrs['style'] = 'min-width: 100%'
        self.fields['content'].widget.attrs['placeholder'] = _('Your review')
        

    class Meta:
        model = Review
        fields = ['name', 'role', 'company', 'content', 'rank', ]
        labels = {
            'name': _('Full Name'),
            'role': _('Role or position'),
            'company': _('Company name'),
            'content': _('Review'),
            'rank': _('Rank us from 1 (bad) to 5 (Excellent)'),
        }