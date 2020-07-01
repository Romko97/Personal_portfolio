from django.shortcuts import render

# Create your views here.
def autobiography_index(request):
    return render(request, "autobiography_index.html")
