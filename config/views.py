from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('login')


def main_page(request):
    return redirect('login')