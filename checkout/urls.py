from django.urls import path
from . import views
from .webhooks import webhook

"""
    Entire code written following Code Institutes Boutique Ado project
    https://github.com/ckz8780/boutique_ado_v1

"""

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
