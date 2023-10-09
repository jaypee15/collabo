from django.shortcuts import render
from .models import Project  

def project_list(request):
    # Retrieve a list of projects from the database 
    projects = Project.objects.all()  

    
    return render(request, 'project_list.html', {'projects': projects})
