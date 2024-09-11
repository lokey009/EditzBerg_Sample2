from django.urls import path
from FirstWebApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('submit/', views.submit_data, name='submit_data'),
]
