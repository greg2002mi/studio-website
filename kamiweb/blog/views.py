from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.models import CustomUser
from .models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Videosam, Wedo, Forwhom
from orders.forms import CallmeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
# from .forms import ()
import os, uuid, json, re, itertools
# from uuid import uuid4
# from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.translation import get_language
from django.core.paginator import Paginator
from orders.views import send_telegram_message
# from django.core.mail import send_mail  # later to send mail - send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
# from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
# from io import BytesIO


# 1 Main Navigation. 
def index(request):
    if request.method == 'POST':
        form = CallmeForm(request.POST)
        if form.is_valid():
            call = form.save(commit=False)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            q1 = form.cleaned_data['question1']
            q2 = form.cleaned_data['question2']
            note = form.cleaned_data['note']
            # Customize the message format
            message = f"*Свяжитесь со мной!*\n\n*Имя:* {name}\n*Email:* {email}\n*Телефон:* {phone}\n*Что интересует:* {q1}\n*Когда удобно поговорить:* {q2} \n*Записка:* {note}"
            send_telegram_message(message)
            call.save()
            return redirect('success')
        else:
            return redirect('fail')
    else:
        if Header.objects.filter(page=1).exists():
            head = Header.objects.filter(page=1).order_by('-created_on').first()
        else:
            return redirect('dashboard.new_he')
        context = {
            'head': head,
            'vidsam': Videosam.objects.order_by('-id').first(),
            'wedo': Wedo.objects.all(),
            'forwhom': Forwhom.objects.all(),
            'reviews': Review.objects.filter(rank__gt=3).order_by('-created_on')[:6],
            'logos': Client.objects.order_by('?')[:10], # random 10
            'form': CallmeForm(),
            }
        return render (request, "index.html", context)

# 2 video cases
def video(request):
    if Header.objects.filter(page=2).exists():
        head = Header.objects.filter(page=2).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    if VidCat.objects.exists():
        category = VidCat.objects.all()
        videos = Vid.objects.all()
        # vids = {cat: cat.vid.all() for cat in category}
    else:
        return redirect('dashboard.new_vcat')
    context = {
        'head': head,
        'category': category,
        'videos': videos,
        }
    return render (request, "vidcase.html", context)

# 3 reels
def reel(request):
    if Header.objects.filter(page=3).exists():
        head = Header.objects.filter(page=3).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    if ReelCat.objects.exists():
        category = ReelCat.objects.all()
        reels = Reel.objects.all()
        allreels = Reel.objects.order_by('category').all()
        # vids = {cat: cat.vid.all() for cat in category}
    else:
        return redirect('dashboard.new_rcat')
    context = {
       'head': head,
       'category': category,
       'reels': reels,
       'allreels': allreels,
        }
    return render (request, "reel.html", context)

# 4 photography
def photogr(request):
    if Header.objects.filter(page=4).exists():
        head = Header.objects.filter(page=4).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    if ImgCat.objects.exists():
        category = ImgCat.objects.all()
        images = Image.objects.all()
        # images = Reel.objects.order_by('category').all()
        # vids = {cat: cat.vid.all() for cat in category}
    else:
        return redirect('dashboard.new_icat')
    context = {
       'head': head,
       'category': category,
       'images': images,
        }
    return render (request, "photography.html", context)

# 5 websites
def web(request):
    if Header.objects.filter(page=6).exists():
        head = Header.objects.filter(page=6).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    if Website.objects.exists():
        images = Website.objects.all()
        # images = Reel.objects.order_by('category').all()
        # vids = {cat: cat.vid.all() for cat in category}
    else:
        return redirect('dashboard.new_g')
    context = {
        'head': head,
        'images': images,
        }
    return render (request, "website.html", context)

# 6 graphic design
def graphics(request):
    if Header.objects.filter(page=5).exists():
        head = Header.objects.filter(page=5).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    images = Gfx.objects.all()
    context = {
        'head': head,
        'images': images,
        }
    return render (request, "graphics.html", context)

# 7 smm
def smm(request):
    if Header.objects.filter(page=7).exists():
        head = Header.objects.filter(page=7).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    smm = SMM.objects.all()
    egsmm = EgSMM.objects.all()
    context = {
        'head': head,
        'smm': smm,
        'egsmm': egsmm,
        }
    return render (request, "smm.html", context)

# 8 sevices
def services(request):
    if Header.objects.filter(page=8).exists():
        head = Header.objects.filter(page=8).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    # service = Service.objects.all()
    lang_dict = {'en': 1, 'ru': 2, 'ko': 3}
    current_language_code = get_language()
    language_int = lang_dict.get(current_language_code, 2)  # Default to 2 if language not found
    service = Service.objects.filter(lang=language_int)
    context = {
        'head': head,
        'service': service,
        }
    return render (request, "services.html", context)

# 9 Customer reviews
def reviews(request):
    if Header.objects.filter(page=11).exists():
        head = Header.objects.filter(page=11).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    # reviews = Review.objects.all()
    latest_reviews = Review.objects.filter(rank__gt=3).order_by('-created_on')[:5]
    
    reviews_list = Review.objects.order_by('-created_on')
    paginator = Paginator(reviews_list, 6)  # Show 6 reviews per page
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
    
    
    context = {
        'head': head,
        'reviews': reviews,
        'latest_reviews': latest_reviews,
        }
    return render (request, "reviews.html", context)

# 10 clients
def client(request):
    if Header.objects.filter(page=10).exists():
        head = Header.objects.filter(page=10).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    clients = Client.objects.all()
    context = {
        'head': head,
        'clients': clients,
        }
    return render (request, "client.html", context)

# 11 about studio
def aboutus(request):
    if Header.objects.filter(page=9).exists():
        head = Header.objects.filter(page=9).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    lang_dict = {'en': 1, 'ru': 2, 'ko': 3}
    current_language_code = get_language()
    language_int = lang_dict.get(current_language_code, 2)  # Default to 2 if language not found
    post = Aboutus.objects.filter(lang=language_int).order_by('created_on')
    context = {
        'head': head,
        'post': post,
        }
    return render (request, "about.html", context)

# 12 contact
def contact(request):
    if request.method == 'POST':
        form = CallmeForm(request.POST)
        if form.is_valid():
            call = form.save(commit=False)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            q1 = form.cleaned_data['question1']
            q2 = form.cleaned_data['question2']
            note = form.cleaned_data['note']
            # Customize the message format
            message = f"*Свяжитесь со мной!*\n\n*Имя:* {name}\n*Email:* {email}\n*Телефон:* {phone}\n*Что интересует:* {q1}\n*Когда удобно поговорить:* {q2} \n*Записка:* {note}"
            send_telegram_message(message)
            call.save()
            return redirect('success')
        else:
            return redirect('fail')
    else:
        if Header.objects.filter(page=12).exists():
            head = Header.objects.filter(page=12).order_by('-created_on').first()
        else:
            head = Header.objects.filter(page=1).order_by('-created_on').first()
        lang_dict = {'en': 1, 'ru': 2, 'ko': 3}
        current_language_code = get_language()
        language_int = lang_dict.get(current_language_code, 2)  # Default to 2 if language not found
        contact = Contact.objects.filter(lang=language_int).order_by('created_on').first()
        context = {
            'head': head,
            'form': CallmeForm(),
            'contact': contact
            }
        return render (request, "contact.html", context)

# 13 contact
# view is in orders app

# 14 contact
def callme(request):
    if Header.objects.filter(page=14).exists():
        head = Header.objects.filter(page=14).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "callme.html", context)

