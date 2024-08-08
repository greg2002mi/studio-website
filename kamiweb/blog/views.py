from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.models import CustomUser
from .models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Call, Order
from .forms import AddYoutubeForm, HeaderForm, AddVidcatForm, AddReelcatForm, AddReelForm, AddImgcatForm, AddImageForm, GfxForm, AddWebsiteForm
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
# from django.core.mail import send_mail  # later to send mail - send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
# from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
# from io import BytesIO


# 1 Main Navigation. 
def index(request):
    if Header.objects.filter(page=1).exists():
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    else:
        return redirect('new_he')
    context = {
        'head': head,
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
        return redirect('new_vcat')
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
        return redirect('new_rcat')
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
        return redirect('new_icat')
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
        return redirect('new_g')
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
    context = {
        'head': head,
        }
    return render (request, "smm.html", context)

# 8 sevices
def services(request):
    if Header.objects.filter(page=8).exists():
        head = Header.objects.filter(page=8).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "services.html", context)

# 9 Customer reviews
def reviews(request):
    if Header.objects.filter(page=11).exists():
        head = Header.objects.filter(page=11).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "reviews.html", context)

# 10 clients
def client(request):
    if Header.objects.filter(page=10).exists():
        head = Header.objects.filter(page=10).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "client.html", context)

# 11 about studio
def aboutus(request):
    if Header.objects.filter(page=9).exists():
        head = Header.objects.filter(page=9).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "about.html", context)

# 12 contact
def contact(request):
    if Header.objects.filter(page=12).exists():
        head = Header.objects.filter(page=12).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "contact.html", context)

# 13 contact
def order(request):
    if Header.objects.filter(page=13).exists():
        head = Header.objects.filter(page=13).order_by('-created_on').first()
    else:
        head = Header.objects.filter(page=1).order_by('-created_on').first()
    context = {
        'head': head,
        }
    return render (request, "order.html", context)

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

# ------------------------- Dashboard ------------------------
@login_required
def dashboard(request):
    context = {
        # 'home': HomePost.objects.all(),
        }
    return render (request, "dashboard.html", context)

@login_required
def d_he(request, entry):
    item = get_object_or_404(Header, pk=entry)
    item.delete()
    messages.success(request, _('Header entry data has been permanently deleted.'))
    return redirect("manageheader")

@login_required
def n_he(request):
    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageheader')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_he')
    else:
        context = {
            'form': HeaderForm(),
            'header_data': Header.objects.all(),
            }
        return render (request, "new_he.html", context)

@login_required
def manageheader(request):
    if Header.objects.exists():
        # h_entry = Header.objects.last()
        # if request.method == 'POST':
        #     form = HeaderForm(request.POST, instance=h_entry)
        #     if form.is_valid():
        #         form.save()
        #         messages.success(request, _("Successfully saved."))
        #         return redirect('manageheader')
        #     else:
        #         messages.error(request, _("Not validated."))
        #         return redirect('manageheader')
        # else:
        context = {
            # 'form': HeaderForm(instance=h_entry),
            'header_data': Header.objects.all(),
            }
        return render (request, "manageheader.html", context)
    else:
        return redirect("new_he")


@login_required
def e_he(request, entry):
    item = get_object_or_404(Header, pk=entry)
    if request.method == 'POST':
        form = HeaderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageheader')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_he', entry=item.id)
    else:
        context={
            'form': HeaderForm(instance=item),
            'header_data': Header.objects.all(),
            }
        return render (request, "new_he.html", context)

#___________ videocase CATEGORY CRUD
@login_required
def d_vcat(request, entry):
    item = get_object_or_404(VidCat, pk=entry)
    item.delete()
    messages.success(request, _('Video category has been permanently deleted.'))
    return redirect("managevideocat")

@login_required
def n_vcat(request):
    if request.method == 'POST':
        form = AddVidcatForm(request.POST)
        if form.is_valid():
            form.save()
              # Save the many-to-many data for the form
            messages.success(request, _("Successfully saved."))
            return redirect('managevideocat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_vcat')
    else:
        context = {
            'form': AddVidcatForm(),
            'vcat_data': VidCat.objects.all(),
            }
        return render (request, "new_vcat.html", context)

@login_required
def managevideocat(request):
    if VidCat.objects.exists():
        # entry = VidCat.objects.last()
        # if request.method == 'POST':
        #     form = AddVidcatForm(request.POST, instance=entry)
        #     if form.is_valid():
        #         form.save()
        #         messages.success(request, _("Successfully saved."))
        #         return redirect('managevideocat')
        #     else:
        #         messages.error(request, _("Not validated."))
        #         return redirect('managevideocat')
        # else:
        context = {
            # 'form': AddVidcatForm(instance=entry),
            'vcat_data': VidCat.objects.all(),
            }
        return render (request, "managevideocat.html", context)
    else:
        return redirect("new_vcat")


@login_required
def e_vcat(request, entry):
    item = get_object_or_404(VidCat, pk=entry)
    if request.method == 'POST':
        form = AddVidcatForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managevideocat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_vcat', entry=item.id)
    else:
        context={
            'form': AddVidcatForm(instance=item),
            'vcat_data': VidCat.objects.all(),
            }
        return render (request, "new_vcat.html", context)


# videocase CRUD ------------------------------------
@login_required
def d_vc(request, entry):
    item = get_object_or_404(Vid, pk=entry)
    item.delete()
    messages.success(request, _('Video data has been permanently deleted.'))
    return redirect("managevideocase")

@login_required
def n_vc(request):
    if VidCat.objects.exists():
        if request.method == 'POST':
            form = AddYoutubeForm(request.POST)
            if form.is_valid():
                vc = form.save(commit=False)
                vc.author = request.user
                # bind reel to category
                cattitle = form.cleaned_data['category']
                cat = get_object_or_404(VidCat, title=cattitle)
                vc.category = cat
                vc.save()
                # vc = form.save(commit=False)
                # vc.author = request.user
                
                # vc.save()
                # form.save_m2m()
               
                
                messages.success(request, _("Successfully saved."))
                return redirect('managevideocase')
            else:
                messages.error(request, _("Not validated."))
                return redirect('new_vc')
        else:
            context = {
                'form': AddYoutubeForm(),
                'vc_data': Vid.objects.all(),
                }
            return render (request, "new_vc.html", context)
    else:    
        return redirect('new_vc2')
    
def n_vc2(request): # create category if there are none before creating video case
    if request.method == 'POST':
        form = AddVidcatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managevideocat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_vc')
    else:
        context = {
            'form': AddVidcatForm(),
            }
        return render (request, "new_vcat.html", context)    

@login_required
def managevideocase(request):
    if Vid.objects.exists():
        context = {
            'vc_data': Vid.objects.all(),
            }
        return render (request, "managevideocase.html", context)
    else:
        return redirect("new_vc")


@login_required
def e_vc(request, entry):
    item = get_object_or_404(Vid, pk=entry)
    if request.method == 'POST':
        form = AddYoutubeForm(request.POST, instance=item)
        if form.is_valid():
            vc = form.save(commit=False)
            # bind reel to category
            cattitle = form.cleaned_data['category']
            cat = get_object_or_404(VidCat, title=cattitle)
            vc.category = cat
            vc.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managevideocase')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_vc', entry=item.id)
    else:
        context={
            'form': AddYoutubeForm(instance=item),
            'vc_data': Vid.objects.all(),
            }
        return render (request, "new_vc.html", context)

#___________ REELS CATEGORY CRUD
@login_required
def d_rcat(request, entry):
    item = get_object_or_404(ReelCat, pk=entry)
    item.delete()
    messages.success(request, _('Reel category has been permanently deleted.'))
    return redirect("managereelcat")

@login_required
def n_rcat(request):
    if request.method == 'POST':
        form = AddReelcatForm(request.POST)
        if form.is_valid():
            form.save()
              # Save the many-to-many data for the form
            messages.success(request, _("Successfully saved."))
            return redirect('managereelcat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_rcat')
    else:
        context = {
            'form': AddReelcatForm(),
            'vcat_data': ReelCat.objects.all(),
            }
        return render (request, "new_rcat.html", context)

@login_required
def managereelcat(request):
    if ReelCat.objects.exists():
        context = {
            'rcat_data': ReelCat.objects.all(),
            }
        return render (request, "managereelcat.html", context)
    else:
        return redirect("new_rcat")


@login_required
def e_rcat(request, entry):
    item = get_object_or_404(ReelCat, pk=entry)
    if request.method == 'POST':
        form = AddReelcatForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managereelcat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_rcat', entry=item.id)
    else:
        context={
            'form': AddReelcatForm(instance=item),
            'vcat_data': ReelCat.objects.all(),
            }
        return render (request, "new_rcat.html", context)


# REEL CRUD -------------------------------------------------------
@login_required
def d_reel(request, entry):
    item = get_object_or_404(Reel, pk=entry)
    item.delete()
    messages.success(request, _('Reel has been permanently deleted.'))
    return redirect("managereel")

@login_required
def n_reel(request):
    if ReelCat.objects.exists():
        if request.method == 'POST':
            form = AddReelForm(request.POST, request.FILES)
            if form.is_valid():
                rl = form.save(commit=False)
                rl.author = request.user
                # bind reel to category
                cattitle = form.cleaned_data['category']
                cat = get_object_or_404(ReelCat, title=cattitle)
                rl.category = cat
                rl.save()
                
                messages.success(request, _("Successfully saved."))
                return redirect('managereel')
            else:
                messages.error(request, _("Not validated."))
                return redirect('new_reel')
        else:
            context = {
                'form': AddReelForm(),
                'reel_data': Reel.objects.all(),
                }
            return render (request, "new_reel.html", context)
    else:    
        return redirect('new_reel2')
 
@login_required
def n_reel2(request): # create category if there are none before creating video case
    if request.method == 'POST':
        form = AddReelcatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managevideocat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_reel')
    else:
        context = {
            'form': AddReelcatForm(),
            }
        return render (request, "new_rcat.html", context)    

@login_required
def managereel(request):
    if Reel.objects.exists():
        context = {
            'reel_data': Reel.objects.all(),
            }
        return render (request, "managereel.html", context)
    else:
        return redirect("new_reel")


@login_required
def e_reel(request, entry):
    item = get_object_or_404(Reel, pk=entry)
    if request.method == 'POST':
        form = AddReelForm(request.POST, instance=item)
        if form.is_valid():
            rl = form.save(commit=False)
            # bind reel to category
            cattitle = form.cleaned_data['category']
            cat = get_object_or_404(ReelCat, title=cattitle)
            rl.category = cat
            rl.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managereel')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_reel', entry=item.id)
    else:
        context={
            'form': AddReelForm(instance=item),
            'reel_data': Reel.objects.all(),
            }
        return render (request, "new_reel.html", context)


#___________ Image CATEGORY CRUD
@login_required
def d_icat(request, entry):
    item = get_object_or_404(ImgCat, pk=entry)
    item.delete()
    messages.success(request, _('Image category has been permanently deleted.'))
    return redirect("manageimgcat")

@login_required
def n_icat(request):
    if request.method == 'POST':
        form = AddImgcatForm(request.POST)
        if form.is_valid():
            form.save()
              # Save the many-to-many data for the form
            messages.success(request, _("Successfully saved."))
            return redirect('manageimgcat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_icat')
    else:
        context = {
            'form': AddImgcatForm(),
            'icat_data': ImgCat.objects.all(),
            }
        return render (request, "new_icat.html", context)

@login_required
def manageimgcat(request):
    if ImgCat.objects.exists():
        context = {
            'icat_data': ImgCat.objects.all(),
            }
        return render (request, "manageimgcat.html", context)
    else:
        return redirect("new_icat")


@login_required
def e_icat(request, entry):
    item = get_object_or_404(ImgCat, pk=entry)
    if request.method == 'POST':
        form = AddImgcatForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageimgcat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_icat', entry=item.id)
    else:
        context={
            'form': AddVidcatForm(instance=item),
            'icat_data': ImgCat.objects.all(),
            }
        return render (request, "new_vcat.html", context)


# Image CRUD -----------------------------------------------------
@login_required
def d_i(request, entry):
    item = get_object_or_404(Image, pk=entry)
    item.delete()
    messages.success(request, _('Image data has been permanently deleted.'))
    return redirect("manageimage")

@login_required
def n_i(request):
    if ImgCat.objects.exists():
        if request.method == 'POST':
            form = AddImageForm(request.POST, request.FILES)
            if form.is_valid():
                i = form.save(commit=False)
                i.author = request.user
                # bind reel to category
                cattitle = form.cleaned_data['category']
                cat = get_object_or_404(ImgCat, title=cattitle)
                i.category = cat
                i.save()
                
                messages.success(request, _("Successfully saved."))
                return redirect('manageimage')
            else:
                messages.error(request, _("Not validated."))
                return redirect('new_i')
        else:
            context = {
                'form': AddImageForm(),
                'i_data': Image.objects.all(),
                }
            return render (request, "new_i.html", context)
    else:    
        return redirect('new_i2')
    
def n_i2(request): # create category if there are none before creating video case
    if request.method == 'POST':
        form = AddImgcatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageimgcat')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_i')
    else:
        context = {
            'form': AddImgcatForm(),
            }
        return render (request, "new_icat.html", context)    

@login_required
def manageimage(request):
    if Image.objects.exists():
        context = {
            'i_data': Image.objects.all(),
            }
        return render (request, "manageimage.html", context)
    else:
        return redirect("new_i")


@login_required
def e_i(request, entry):
    item = get_object_or_404(Image, pk=entry)
    if request.method == 'POST':
        form = AddImageForm(request.POST, instance=item)
        if form.is_valid():
            i = form.save(commit=False)
            # bind reel to category
            cattitle = form.cleaned_data['category']
            cat = get_object_or_404(ImgCat, title=cattitle)
            i.category = cat
            i.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageimage')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_i', entry=item.id)
    else:
        context={
            'form': AddImageForm(instance=item),
            'i_data': Image.objects.all(),
            }
        return render (request, "new_i.html", context)

# Gfx CRUD ----------------------------------------------------
@login_required
def d_g(request, entry):
    item = get_object_or_404(Gfx, pk=entry)
    item.delete()
    messages.success(request, _('Graphic design Image data has been permanently deleted.'))
    return redirect("managegfx")

@login_required
def n_g(request):
    if request.method == 'POST':
        form = GfxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # i = form.save(commit=False)
            # i.author = request.user
            # # bind reel to category
            # cattitle = form.cleaned_data['category']
            # cat = get_object_or_404(ImgCat, title=cattitle)
            # i.category = cat
            # i.save()
            
            messages.success(request, _("Successfully saved."))
            return redirect('managegfx')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_g')
    else:
        context = {
            'form': GfxForm(),
            'g_data': Gfx.objects.all(),
            }
        return render (request, "new_g.html", context) 

@login_required
def managegfx(request):
    if Gfx.objects.exists():
        context = {
            'g_data': Gfx.objects.all(),
            }
        return render (request, "managegfx.html", context)
    else:
        return redirect("new_g")


@login_required
def e_g(request, entry):
    item = get_object_or_404(Gfx, pk=entry)
    if request.method == 'POST':
        form = GfxForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # i = form.save(commit=False)
            # # bind reel to category
            # cattitle = form.cleaned_data['category']
            # cat = get_object_or_404(ImgCat, title=cattitle)
            # i.category = cat
            # i.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managegfx')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_g', entry=item.id)
    else:
        context={
            'form': GfxForm(instance=item),
            'g_data': Gfx.objects.all(),
            }
        return render (request, "new_g.html", context)
    
    
# Website CRUD ----------------------------------------------------
@login_required
def d_w(request, entry):
    item = get_object_or_404(Website, pk=entry)
    item.delete()
    messages.success(request, _('Web design data has been permanently deleted.'))
    return redirect("manageweb")

@login_required
def n_w(request):
    if request.method == 'POST':
        form = AddWebsiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, _("Successfully saved."))
            return redirect('manageweb')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_w')
    else:
        context = {
            'form': AddWebsiteForm(),
            'g_data': Website.objects.all(),
            }
        return render (request, "new_w.html", context) 

@login_required
def manageweb(request):
    if Website.objects.exists():
        context = {
            'w_data': Website.objects.all(),
            }
        return render (request, "manageweb.html", context)
    else:
        return redirect("new_w")


@login_required
def e_w(request, entry):
    item = get_object_or_404(Website, pk=entry)
    if request.method == 'POST':
        form = AddWebsiteForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageweb')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_w', entry=item.id)
    else:
        context={
            'form': AddWebsiteForm(instance=item),
            'w_data': Website.objects.all(),
            }
        return render (request, "new_w.html", context)    
    
# ------------------------- Dashboard ------------------------