from django.shortcuts import render
from .models import Certificates

def certificates_index(request):
    certificates = Certificates.objects.all()
    return render(request, "certificates_index.html", {'title':'CERTIFICATE', 'certificates': certificates})


def certificates_detail(request, pk):
    certificate = Certificates.objects.get(pk=pk)
    context = {'certificate': certificate}
    return render(request, 'certificate_detail.html', context)