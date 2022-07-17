from operator import index
from django import views
from django.urls import path
from core import views
urlpatterns = [
    path('', views.index, name = "index"),
]