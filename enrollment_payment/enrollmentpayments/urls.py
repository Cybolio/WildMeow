from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home', views.home_view, name='home'),
    path('edit-profile', views.edit_profile_view, name='edit_profile'),
    path('logoff', views.logoff_view, name='logoff'),
    path('enrollment/addNewUser', views.add_new_user, name='add_new_user'),
    path('enrollment/addNewPayment', views.add_new_payment, name='add_new_payment'),
    path('enrollment/addNewWaitlist', views.add_new_waitlist, name='add_new_waitlist'),
]