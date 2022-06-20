from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import CreateView
def profile(request):
    if request.user.is_superuser:
        template = "profile_admin.html"
    else:
        template = "profile_nonadmin.html"
    return render(request, template, {'user': request.user, 'equals': "=" * len(request.user.username) + "======"})
def home(request):
    return render(request, "AllHome2.html", {'user': request.user})
class UserCreateView(CreateView):
    model = User
    fields = ["username", "password"]
    template_name = "new_account_nonadmin.html"
    success_url = "profile"
