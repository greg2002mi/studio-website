from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from users.models import CustomUser
from orders.models import Order, Call
from blog.models import Global, Header, ImgCat, Image, VidCat, Vid, ReelCat, Reel, Gfx, Service, Website, SMM, EgSMM, Aboutus, Client, Review, Contact, Videosam, Wedo, Forwhom
from .forms import AddYoutubeForm, HeaderForm, AddVidcatForm, AddReelcatForm, AddReelForm, AddImgcatForm, AddImageForm, GfxForm, AddWebsiteForm, SmmForm, EgSmmForm, ServiceForm, ClientForm, AboutusForm, ContactInfoForm, ForwhomForm, WedoForm, VideosamForm
from orders.forms import OrderForm, CallmeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# ------------------------- Dashboard ------------------------
@login_required
def dashboard(request):
    orders = Order.objects.all().order_by('-created_on')
    orders_page = request.GET.get('orders_page', 1)  # Use a specific page parameter for orders
    paginator_orders = Paginator(orders, 10)  # Show 10 orders per page
    try:
        orders_paginated = paginator_orders.page(orders_page)
    except PageNotAnInteger:
        orders_paginated = paginator_orders.page(1)
    except EmptyPage:
        orders_paginated = paginator_orders.page(paginator_orders.num_pages)
    
    # Paginate calls
    calls = Call.objects.all().order_by('-created_on')
    calls_page = request.GET.get('calls_page', 1)  # Use a specific page parameter for calls
    paginator_calls = Paginator(calls, 10)
    try:
        calls_paginated = paginator_calls.page(calls_page)
    except PageNotAnInteger:
        calls_paginated = paginator_calls.page(1)
    except EmptyPage:
        calls_paginated = paginator_calls.page(paginator_calls.num_pages) 
    context = {
        'orders': orders_paginated,
        'calls': calls_paginated,
        'user': request.user,
        }
    return render (request, "dashboard.html", context)

@login_required
def edit_o(request, ordid):
    item = get_object_or_404(Order, pk=ordid)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully changed."))
            return redirect('dashboard')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_order', ordid=item.id)
    else:
        context={
            'form': OrderForm(instance=item),
            'user': request.user,
            }
        return render (request, "edit_o.html", context)
    
@login_required
def e_call(request, ordid):
    item = get_object_or_404(Call, pk=ordid)
    if request.method == 'POST':
        form = CallmeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully changed."))
            return redirect('dashboard')
        else:
            messages.error(request, _("Not validated."))
            return redirect('e_call', ordid=item.id)
    else:
        context={
            'form': CallmeForm(instance=item),
            'user': request.user,
            }
        return render (request, "edit_o.html", context)    
    
@login_required
def o_pr(request, ordid, s):
    item = get_object_or_404(Order, pk=ordid)
    item.status = s
    item.save()
    return redirect('dashboard')

@login_required
def c_pr(request, ordid, s):
    item = get_object_or_404(Call, pk=ordid)
    item.status = s
    item.save()
    return redirect('dashboard')
    

# ------------- Header ------------------
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
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
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
                'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_vcat.html", context)    

@login_required
def managevideocase(request):
    if Vid.objects.exists():
        context = {
            'vc_data': Vid.objects.all(),
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_rcat.html", context)

@login_required
def managereelcat(request):
    if ReelCat.objects.exists():
        context = {
            'rcat_data': ReelCat.objects.all(),
            'user': request.user,
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
            'user': request.user,
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
                'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_rcat.html", context)    

@login_required
def managereel(request):
    if Reel.objects.exists():
        context = {
            'reel_data': Reel.objects.all(),
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_icat.html", context)

@login_required
def manageimgcat(request):
    if ImgCat.objects.exists():
        context = {
            'icat_data': ImgCat.objects.all(),
            'user': request.user,
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
            'user': request.user,
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
                'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_icat.html", context)    

@login_required
def manageimage(request):
    if Image.objects.exists():
        context = {
            'i_data': Image.objects.all(),
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_g.html", context) 

@login_required
def managegfx(request):
    if Gfx.objects.exists():
        context = {
            'g_data': Gfx.objects.all(),
            'user': request.user,
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
            'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_w.html", context) 

@login_required
def manageweb(request):
    if Website.objects.exists():
        context = {
            'w_data': Website.objects.all(),
            'user': request.user,
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
            'user': request.user,
            }
        return render (request, "new_w.html", context)    

# SMM CRUD ----------------------------------------------------
@login_required
def d_s(request, entry):
    item = get_object_or_404(SMM, pk=entry)
    item.delete()
    messages.success(request, _('SMM data has been permanently deleted.'))
    return redirect("managesmm")

@login_required
def n_s(request):
    if request.method == 'POST':
        form = SmmForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, _("Successfully saved."))
            return redirect('managesmm')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_s')
    else:
        context = {
            'form': SmmForm(),
            'user': request.user,
            # 'smm_data': SMM.objects.order_by('-created_on').first(),
            }
        return render (request, "new_s.html", context) 

@login_required
def managesmm(request):
    if SMM.objects.exists():
        context = {
            'smm_data': SMM.objects.all(),
            'user': request.user,
            }
        return render (request, "managesmm.html", context)
    else:
        return redirect("new_s")


@login_required
def e_s(request, entry):
    item = get_object_or_404(SMM, pk=entry)
    if request.method == 'POST':
        form = SmmForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managesmm')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_s', entry=item.id)
    else:
        context={
            'form': SmmForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_s.html", context) 

# EgSMM CRUD ----------------------------------------------------
@login_required
def d_es(request, entry):
    item = get_object_or_404(EgSMM, pk=entry)
    item.delete()
    messages.success(request, _('SMM example has been permanently deleted.'))
    return redirect("manageegsmm")

@login_required
def n_es(request):
    if request.method == 'POST':
        form = EgSmmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, _("Successfully saved."))
            return redirect('manageegsmm')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_es')
    else:
        context = {
            'form': EgSmmForm(),
            'user': request.user,
            }
        return render (request, "new_es.html", context) 

@login_required
def manageegsmm(request):
    if EgSMM.objects.exists():
        context = {
            'egsmm_data': EgSMM.objects.all(),
            'user': request.user,
            }
        return render (request, "manageegsmm.html", context)
    else:
        return redirect("new_es")


@login_required
def e_es(request, entry):
    item = get_object_or_404(EgSMM, pk=entry)
    if request.method == 'POST':
        form = EgSmmForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageegsmm')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_es', entry=item.id)
    else:
        context={
            'form': EgSmmForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_es.html", context) 

# Service CRUD ----------------------------------------------------
@login_required
def d_serv(request, entry):
    item = get_object_or_404(Service, pk=entry)
    item.delete()
    messages.success(request, _('Service has been permanently deleted.'))
    return redirect("manageserv")

@login_required
def n_serv(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            serv = form.save(commit=False)
            serv.author = request.user
            serv.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageserv')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_serv')
    else:
        context = {
            'form': ServiceForm(),
            'user': request.user,
            # 'smm_data': SMM.objects.order_by('-created_on').first(),
            }
        return render (request, "new_serv.html", context) 

@login_required
def manageserv(request):
    if Service.objects.exists():
        context = {
            'serv_data': Service.objects.all(),
            'user': request.user,
            }
        return render (request, "manageserv.html", context)
    else:
        return redirect("new_serv")


@login_required
def e_serv(request, entry):
    item = get_object_or_404(Service, pk=entry)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=item)
        if form.is_valid():
            serv = form.save(commit=False)
            serv.author = request.user
            serv.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageserv')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_serv', entry=item.id)
    else:
        context={
            'form': ServiceForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_serv.html", context) 
    
# Clients CRUD ----------------------------------------------------
@login_required
def d_cl(request, entry):
    item = get_object_or_404(Client, pk=entry)
    item.delete()
    messages.success(request, _('Client data has been permanently deleted.'))
    return redirect("manageclient")

@login_required
def n_cl(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
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
            return redirect('manageclient')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_cl')
    else:
        context = {
            'form': ClientForm(),
            'user': request.user,
            }
        return render (request, "new_cl.html", context) 

@login_required
def manageclient(request):
    if Client.objects.exists():
        context = {
            'cl_data': Client.objects.all(),
            'user': request.user,
            }
        return render (request, "manageclient.html", context)
    else:
        return redirect("new_cl")


@login_required
def e_cl(request, entry):
    item = get_object_or_404(Client, pk=entry)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # i = form.save(commit=False)
            # # bind reel to category
            # cattitle = form.cleaned_data['category']
            # cat = get_object_or_404(ImgCat, title=cattitle)
            # i.category = cat
            # i.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageclient')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_cl', entry=item.id)
    else:
        context={
            'form': ClientForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_cl.html", context)
    
# About us CRUD ----------------------------------------------------
@login_required
def d_au(request, entry):
    item = get_object_or_404(Aboutus, pk=entry)
    item.delete()
    messages.success(request, _('Aboutus post has been permanently deleted.'))
    return redirect("manageaboutus")

@login_required
def n_au(request):
    if request.method == 'POST':
        form = AboutusForm(request.POST, request.FILES)
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
            return redirect('manageaboutus')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_au')
    else:
        context = {
            'form': AboutusForm(),
            'user': request.user,
            }
        return render (request, "new_au.html", context) 

@login_required
def manageaboutus(request):
    if Aboutus.objects.exists():
        context = {
            'au_data': Aboutus.objects.all(),
            'user': request.user,
            }
        return render (request, "manageaboutus.html", context)
    else:
        return redirect("new_au")


@login_required
def e_au(request, entry):
    item = get_object_or_404(Aboutus, pk=entry)
    if request.method == 'POST':
        form = AboutusForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully saved."))
            return redirect('manageaboutus')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_au', entry=item.id)
    else:
        context={
            'form': AboutusForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_au.html", context)

# Review CRUD ----------------------------------------------------
@login_required
def d_rw(request, entry):
    item = get_object_or_404(Review, pk=entry)
    item.delete()
    messages.success(request, _('Review has been permanently deleted.'))
    return redirect("managereview")

@login_required
def managereview(request):
    context = {
        'rw_data': Review.objects.all(),
        'user': request.user,
        }
    return render (request, "managereview.html", context)


# Contact info CRUD ----------------------------------------------------
@login_required
def d_ct(request, entry):
    item = get_object_or_404(Contact, pk=entry)
    item.delete()
    messages.success(request, _('Contacts page has been permanently deleted.'))
    return redirect("managecontactus")

@login_required
def n_ct(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managecontactus')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_ct')
    else:
        context = {
            'form': ContactInfoForm(),
            'user': request.user,
            }
        return render (request, "new_ct.html", context) 

@login_required
def managecontactus(request):
    if Contact.objects.exists():
        context = {
            'ct_data': Contact.objects.all(),
            'user': request.user,
            }
        return render (request, "managecontactus.html", context)
    else:
        return redirect("new_ct")


@login_required
def e_ct(request, entry):
    item = get_object_or_404(Contact, pk=entry)
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # i = form.save(commit=False)
            # # bind reel to category
            # cattitle = form.cleaned_data['category']
            # cat = get_object_or_404(ImgCat, title=cattitle)
            # i.category = cat
            # i.save()
            messages.success(request, _("Successfully saved."))
            return redirect('managecontactus')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_ct', entry=item.id)
    else:
        context={
            'form': ContactInfoForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_ct.html", context)

# Main CRUD ----------------------------------------------------

# delete videosamples
@login_required
def d_vs(request, entry):
    item = get_object_or_404(Videosam, pk=entry)
    item.delete()
    messages.success(request, _('Promo videos set has been permanently deleted.'))
    return redirect("managemain")

# delete our services
@login_required
def d_wd(request, entry):
    item = get_object_or_404(Wedo, pk=entry)
    item.delete()
    messages.success(request, _('Our service has been permanently deleted.'))
    return redirect("managemain")

# delete what we accomplish
@login_required
def d_fw(request, entry):
    item = get_object_or_404(Forwhom, pk=entry)
    item.delete()
    messages.success(request, _('Entry has been permanently deleted.'))
    return redirect("managemain")

@login_required
def n_vs(request):
    if request.method == 'POST':
        form = VideosamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managemain')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_vs')
    else:
        context = {
            'form': VideosamForm(),
            'user': request.user,
            }
        return render (request, "new_main.html", context) 

@login_required
def n_wd(request):
    if request.method == 'POST':
        form = WedoForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managemain')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_wd')
    else:
        context = {
            'form': WedoForm(),
            'user': request.user,
            }
        return render (request, "new_main.html", context)

@login_required
def n_fw(request):
    if request.method == 'POST':
        form = ForwhomForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managemain')
        else:
            messages.error(request, _("Not validated."))
            return redirect('new_fw')
    else:
        context = {
            'form': ForwhomForm(),
            'user': request.user,
            }
        return render (request, "new_main.html", context)


@login_required
def managemain(request):
    context = {
        'vs_data': Videosam.objects.all(),
        'wd_data': Wedo.objects.all(),
        'fw_data': Forwhom.objects.all(),
        'user': request.user,
        }
    return render (request, "managemain.html", context)


@login_required
def e_vs(request, entry):
    item = get_object_or_404(Videosam, pk=entry)
    if request.method == 'POST':
        form = VideosamForm(request.POST, instance=item)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managemain')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_vs', entry=item.id)
    else:
        context = {
            'form': VideosamForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_main.html", context) 

@login_required
def e_wd(request, entry):
    item = get_object_or_404(Wedo, pk=entry)
    if request.method == 'POST':
        form = WedoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managemain')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_wd', entry=item.id)
    else:
        context = {
            'form': WedoForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_main.html", context)

@login_required
def e_fw(request, entry):
    item = get_object_or_404(Forwhom, pk=entry)
    if request.method == 'POST':
        form = ForwhomForm(request.POST, instance=item)
        if form.is_valid():
            form.save()            
            messages.success(request, _("Successfully saved."))
            return redirect('managemain')
        else:
            messages.error(request, _("Not validated."))
            return redirect('edit_fw', entry=item.id)
    else:
        context = {
            'form': ForwhomForm(instance=item),
            'user': request.user,
            }
        return render (request, "new_main.html", context)