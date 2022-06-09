from django.http import HttpResponse
from django.urls import path, include
from adminApp import views
urlpatterns = [
    path('users/', views.users),
    path('users/remove/', lambda request: HttpResponse("not implemented")),
    path('users/talk/', lambda reguest: HttpResponse("not implemented"))
]