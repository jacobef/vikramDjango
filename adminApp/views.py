from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from adminApp.models import message
import re
# Create your views here.
from django.views.generic import CreateView
from adminApp import models
def users(request):
    return render(request, "users.html", {"A_users" : User.objects.all(), "users" : len(User.objects.all())})
@login_required
def viewListOfMessages(request):
    if request.user.is_superuser:
        template = "messages_admin.html"
    else:
        template = "messages_nonadmin.html"
    return render(request, template, {"UserSent" : None, "Messages" : FilterToUser(request)})
def FilterToUser(request):
    return message.objects.filter(To=request.user)
def MessagesHome(request):
    if request.user.is_superuser:
        template = "MessagesHome_admin.html"
    else:
        template = "messagesHome_nonadmin.html"
    return render(request, template)
class ViewMessages(CreateView):
    model = message
    fields = ["inputField", "To"]
    template_name = "messages2_nonadmin.html"
    success_url = "/messages"
    pass

def view_messages(request):
    if request.user.is_superuser:
        return ViewMessages.as_view(template_name="messages2_admin.html")(request)
    else:
        return ViewMessages.as_view(template_name="messages2_nonadmin.html")(request)

def messages(request):
    return redirect("/messages/view/")
