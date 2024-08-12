from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("order/<int:ordid>", views.order, name="order"),
    path("success", views.success, name="success"),
    path("fail", views.fail, name="fail"),
    path("write_review", views.write, name="write_review"),
]