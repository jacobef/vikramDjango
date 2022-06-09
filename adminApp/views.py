from django.contrib.auth.models import User
from django.shortcuts import render
import re
# Create your views here.
def users(request):
    user = 0
    n = []
    k = User.objects.all()
    m = 0
    for i in range(0, len(k)):
        n.append(k[m])
        m += 1
    t = "*\n".join([str(elem) for elem in n])
    for users in User.objects.all():
        user += 1
    return render(request, "users.html", {"user" : user, "A_users" : User.objects.all(), "T_users" : t})