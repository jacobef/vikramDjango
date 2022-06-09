from django.contrib.auth.models import User
from django.shortcuts import render
import re
# Create your views here.
def users(request):
    return render(request, "users.html", {"A_users" : User.objects.all(), "users" : len(User.objects.all())})