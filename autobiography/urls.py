from django.urls import path
from . import views

urlpatterns = [
    path('',views.autobiography_index,name="autobiography_index"),
]