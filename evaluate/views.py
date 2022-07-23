from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Number


def index(request):
    context = {'num': Number.objects.all()[0]}
    return render(request, 'evaluate/stuff.html', context)


def add(request):
    num = Number.objects.all()[0]
    num.number = num.number + 1
    num.save()
    return redirect('index')


def subtract(request):
    num = Number.objects.all()[0]
    num.number = num.number - 1
    num.save()
    return redirect('index')


def reset(request):
    num = Number.objects.all()[0]
    num.number = 0
    num.save()
    return redirect('index')