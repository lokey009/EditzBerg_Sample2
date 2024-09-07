from django.urls import path
from FirstWebApp import views

urlpatterns = [
    path("", views.home, name="home"),
]
