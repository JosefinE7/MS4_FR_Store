from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_likes, name='view_likes')
]
