from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model


# Create your views here.
# def home_page(request):
#    return render(request, 'home.html')


def login_view(request):
   return render(request,'log_int.html')


def register_view(request):
   return render(request,'register.html')