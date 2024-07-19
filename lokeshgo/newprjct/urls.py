from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_newprjct, name='all_newprjct'),
]