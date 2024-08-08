from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
# 2 video cases
    path("vidcase", views.video, name="vidcase"),
# categories
    # path("vidcasecat/<int:catid>", views.videocat, name="vidcasecat"),
# 3 reels
    path("reel", views.reel, name="reel"),
# categories
    # path("reelcat/<int:catid>", views.reelcat, name="reelcat"),
# 4 photography
    path("photography", views.photogr, name="photography"),
# 5 websites
    path("web_design", views.web, name="web_design"),
# 6 graphic design
    path("graphics", views.graphics, name="graphics"),
# 7 smm
    path("smm", views.smm, name="smm"),
# 8 sevices
    path("services", views.services, name="services"),
# 9 Customer reviews
    path("reviews", views.reviews, name="reviews"),
# 10 clients
    path("our_clients", views.client, name="our_clients"),
# 11 about studio
    path("aboutus", views.aboutus, name="aboutus"),
# 12 contact
    path("contact", views.contact, name="contact"),
# 13 make order
    path("make_order", views.order, name="make_order"),
# 14 call me
    path("call_me", views.callme, name="call_me"),
# 15 dashboard
    path("dashboard", views.dashboard, name="dashboard"),
    # ---------- header ----------
    path("manageheader", views.manageheader, name="manageheader"),
    path("new_he", views.n_he, name="new_he"),
    path("edit_he/<int:entry>", views.e_he, name="edit_he"),
    path("delete_he/<int:entry>", views.d_he, name="delete_he"),
    # ---------- vcategory ----------
    path("managevideocat", views.managevideocat, name="managevideocat"),
    path("new_vcat", views.n_vcat, name="new_vcat"),
    path("edit_vcat/<int:entry>", views.e_vcat, name="edit_vcat"),
    path("delete_vcat/<int:entry>", views.d_vcat, name="delete_vcat"),
    # ---------- video case ----------
    path("managevideocase", views.managevideocase, name="managevideocase"),
    path("new_vc", views.n_vc, name="new_vc"),
    path("new_vc2", views.n_vc2, name="new_vc2"), # to first create category before saving the video case
    path("edit_vc/<int:entry>", views.e_vc, name="edit_vc"),
    path("delete_vc/<int:entry>", views.d_vc, name="delete_vc"),
    # ---------- reel category ----------
    path("managereelcat", views.managereelcat, name="managereelcat"),
    path("new_rcat", views.n_rcat, name="new_rcat"),
    path("edit_rcat/<int:entry>", views.e_rcat, name="edit_rcat"),
    path("delete_rcat/<int:entry>", views.d_rcat, name="delete_rcat"),
    # ---------- reel ----------
    path("managereel", views.managereel, name="managereel"),
    path("new_reel", views.n_reel, name="new_reel"),
    path("new_reel2", views.n_reel2, name="new_reel2"), # to first create category before saving a reel
    path("edit_reel/<int:entry>", views.e_reel, name="edit_reel"),
    path("delete_reel/<int:entry>", views.d_reel, name="delete_reel"),
    # ---------- icategory ----------
    path("manageimgcat", views.manageimgcat, name="manageimgcat"),
    path("new_icat", views.n_icat, name="new_icat"),
    path("edit_icat/<int:entry>", views.e_icat, name="edit_icat"),
    path("delete_icat/<int:entry>", views.d_icat, name="delete_icat"),
    # ---------- Image ----------
    path("manageimage", views.manageimage, name="manageimage"),
    path("new_i", views.n_i, name="new_i"),
    path("new_i2", views.n_i2, name="new_i2"), # to first create category before saving an image
    path("edit_i/<int:entry>", views.e_i, name="edit_i"),
    path("delete_i/<int:entry>", views.d_i, name="delete_i"),
    # ---------- Gfx ----------
    path("managegfx", views.managegfx, name="managegfx"),
    path("new_g", views.n_g, name="new_g"),
    path("edit_g/<int:entry>", views.e_g, name="edit_g"),
    path("delete_g/<int:entry>", views.d_g, name="delete_g"),
    # ---------- Website design ----------
    path("manageweb", views.manageweb, name="manageweb"),
    path("new_w", views.n_w, name="new_w"),
    path("edit_w/<int:entry>", views.e_w, name="edit_w"),
    path("delete_w/<int:entry>", views.d_w, name="delete_w"),
    ]