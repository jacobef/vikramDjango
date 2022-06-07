from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import CreateView


def hi(request, some_int):
    print(some_int)
    return render(request, "img.html")
def write(request):
    return render(request, "html.html")

def profile(request):
    return render(request, "profile.html", {'user': request.user, 'equals': "=" * len(request.user.username) + "======"})

class UserCreateView(CreateView):
    model = User
    fields = ["username", "password"]
    template_name = "new_account.html"
    success_url = "profile"
    pass