from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.inventory_home, name='inventory_home'),

]