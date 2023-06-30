from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index(request):
    return render(request, 'pages/index.html')


