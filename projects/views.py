from django.shortcuts import render
from projects.models import Project

def project_index():
    projects = Project.objects.all()
    context =   {"projects": projects}
    return render( request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # pk primary key, 
    context = { "project":project}
    return render ( request, 'project_detail', context)

