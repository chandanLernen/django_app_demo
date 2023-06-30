from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def about_index(request):
    return render(request, 'about/index.html')


def soy(request):
    return render(request, 'about/soy.html')


def contact_us(request):
    return render(request, 'about/contact_us.html')


