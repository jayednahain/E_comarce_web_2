from django.contrib import admin
from django.urls import path,include
from home_app.views import home_page

urlpatterns = [
    path('',home_page,name='home_page')
]