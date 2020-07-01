from django.urls import path
from . import views

urlpatterns = [
    path('',views.certificates_index,name="certificates_index"),
]