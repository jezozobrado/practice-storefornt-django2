from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def detail(request):
    context = {}
    return render(request, 'store/detail.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def login(request):
    context = {}
    return render(request, 'user/login.html', context)


def register(request):
    context = {}
    return render(request, 'user/register.html', context)


def logout(request):
    context = {}
    return render(request, 'user/logout.html', context)
