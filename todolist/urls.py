from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url('', views.todo_index, name="todo_index"),
]