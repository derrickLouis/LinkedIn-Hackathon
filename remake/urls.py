from django.urls import path
from .views import email_gather
from . import views

urlpatterns = [
    path('', email_gather, name='email_gather'),
    path('', views.index, name='index'),
    path('post/', views.second_page, name='post'),
]