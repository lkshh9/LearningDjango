from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_newprjct, name='all_newprjct'),
    path('<int:prj_id>/', views.prj_detail, name='prj_detail'),
]
