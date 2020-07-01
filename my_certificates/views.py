from django.shortcuts import render


def certificates_index(request):
    return render(request, "certificates_index.html")
