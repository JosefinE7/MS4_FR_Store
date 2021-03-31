from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/about/', views.about, name='about'),
]
