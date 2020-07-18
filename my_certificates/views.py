from django.shortcuts import render
from .models import Certificates

def certificates_index(request):
    certificates = Certificates.objects.all()
    return render(request, "certificates_index.html", {'title':'CERTIFICATE', 'certificates': certificates})
