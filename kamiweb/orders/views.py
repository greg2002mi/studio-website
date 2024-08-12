from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from users.models import CustomUser
from blog.models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact
from .forms import OrderForm, WriteForm, CallmeForm
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import os, uuid, json, re, requests
from django.conf import settings

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': settings.CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)
    return response.json()

def order(request, ordid):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            chosen = get_object_or_404(Service, pk=ordid)
            currency_dict = {1: 'KRW', 2: 'USD', 3: 'РУБЛ'}
            curr = currency_dict.get(chosen.currency, 'Необозначено')
            lang_dict = {1: 'Английский', 2: 'Русский', 3: 'Корейский'}
            lang_text = lang_dict.get(chosen.lang, 'Необозначено')
            # Customize the message format
            message = f"*Новый заказ!*\n\n*Имя:* {name}\n*Email:* {email}\n*Телефон:* {phone}\n*Заказ:* {chosen.title}\n*Цена:* {chosen.price} ({curr})\n*Язык:* {lang_text}"
            order.note = message
            send_telegram_message(message)
            order.save()
            return redirect('success')
        else:
            return redirect('fail')
    else:
        if Header.objects.filter(page=20).exists():
            head = Header.objects.filter(page=20).order_by('-created_on').first()
        else:
            head = Header.objects.filter(page=1).order_by('-created_on').first()    
        service = get_object_or_404(Service, pk=ordid)
        context = {
            'head': head,
            'ordid': ordid,
            'form': OrderForm(),
            'service': service,
            }
        return render (request, "order.html", context)

def success(request):
    if Header.objects.filter(page=98).exists():
        head = Header.objects.filter(page=98).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "success.html", context)

def fail(request):
    if Header.objects.filter(page=99).exists():
        head = Header.objects.filter(page=99).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "error.html", context)

def write(request):
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            return redirect('fail')
    else:    
        if Header.objects.filter(page=21).exists():
            head = Header.objects.filter(page=21).order_by('-created_on').first()
        else:
            head = Header.objects.filter(page=1).order_by('-created_on').first()
        
        context = {
            'head': head,
            'form': WriteForm(),
            }
        return render (request, "write.html", context)

def call_me(request):
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
        if Header.objects.filter(page=20).exists():
            head = Header.objects.filter(page=20).order_by('-created_on').first()
        else:
            head = Header.objects.filter(page=1).order_by('-created_on').first()    
        
        context = {
            'head': head,
            # 'ordid': ordid,
            'form': CallmeForm(),
            # 'service': service,
            }
        return render (request, "contact.html", context)
