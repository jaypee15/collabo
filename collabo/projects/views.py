from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from .models import Project  

def project_list(request):

    # Define mappping for project status to background color
  

    # Retrieve a list of projects from the database 
    projects = Project.objects.all()  

    context ={
        "projects":projects,   
    }
    
    return render(request, "projects/app.html", context)

@require_http_methods(["POST"])
def search(request):
    search_text = request.POST.get("search")

    # Look up all projects that contain the text
    results = Project.objects.filter(
        Q(title__icontains=search_text) | Q(tags__name__icontains=search_text) 
        | Q(skills_required__name__icontains=search_text)
    ).distinct()

    context = {"results": results}
    return render(request, "projects/partials/search.html", context)


