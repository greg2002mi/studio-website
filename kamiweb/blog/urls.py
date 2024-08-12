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
    # url is in orders app
# 14 call me
    path("call_me", views.callme, name="call_me"),
    ]