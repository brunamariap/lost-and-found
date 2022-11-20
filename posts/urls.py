from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('items/', views.items, name='items'),
    path('delivered-items', views.deliveredItems, name='delivered-items'),
    path('expired-items', views.expiredItems, name='expired-items'),
]
