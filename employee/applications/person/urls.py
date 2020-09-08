from django.contrib import admin
from django.urls import path


def from_apps(self):
    print("Hello from person side")

urlpatterns = [
    path('person/', from_apps),
]