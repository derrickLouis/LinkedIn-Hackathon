from django.urls import path
from .views import email_gather

urlpatterns = [
    path('email_gather/', email_gather, name='email_gather'),
]
