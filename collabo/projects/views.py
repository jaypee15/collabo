from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from .models import Project  

def project_list(request):

  
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


def project_detail(request, pk):
    # get project with the given pk or return 404
    project = get_object_or_404(Project, pk=pk)

    context = {"project": project}

    return render(request, "projects/project_detail.html", context)



