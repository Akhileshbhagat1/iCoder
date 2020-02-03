from django.contrib import auth
from django.shortcuts import render, redirect


def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
