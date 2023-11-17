
from django.urls import path

from . import views

app_name = "rest"

urlpatterns = [
    path("", views.about, name="about"),
    path("blog", views.blog, name="blog"),

   # path("contact", views.contact, name="contact"),
 #   path("menu", views.menu, name="menu"),
   # path("reservation", views.reservation, name="reservation")


]