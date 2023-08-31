from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('logout/', views.signout, name='logout'),
    path('register/', views.signup, name='register'),
    path('record/<int:pk>', views.data_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    
]
