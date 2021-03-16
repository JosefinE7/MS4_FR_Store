from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_likes, name='view_likes'),
    path('add/<item_id>/', views.add_to_likes, name='add_to_likes'),

]
