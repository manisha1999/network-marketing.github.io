from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="ShopHome"),
    #path("about/", views.about,name="aboutus"),
    path("business/", views.business,name="business"),
    path("product/", views.product,name="product"),
    path("rewards/", views.rewards,name="reward"),
path("login/", views.login,name="login"),
path("join/", views.join,name="join"),
path("contact/", views.contact,name="contactus"),
]