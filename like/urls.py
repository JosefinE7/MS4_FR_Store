from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_like, name='view_like'),
    path('add/<item_id>/', views.add_to_like, name='add_to_like'),

]
