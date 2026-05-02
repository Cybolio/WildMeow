from django.urls import path
from . import views

urlpatterns = [
    path('addNewUser', views.addNewUser, name='addNewUser'),
    path('addNewPayment', views.addNewPayment, name='addNewPayment'),
    path('addNewWaitlist', views.addNewWaitlist, name='addNewWaitlist'),
]