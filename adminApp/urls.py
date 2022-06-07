from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('users/', lambda request: HttpResponse("not implemented")),
    path('users/remove/', lambda request: HttpResponse("not implemented")),
    path('users/talk/', lambda reguest: HttpResponse("not implemented"))
]