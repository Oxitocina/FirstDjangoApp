from django.contrib import admin
from django.urls import path


def from_apps(self):
    print("Hello from department side")

urlpatterns = [
    path('department/', from_apps),
]