from django.urls import path

from .views import (
    project_list,
   
)

app_name = "projects"
urlpatterns = [
    path("projects/", view=project_list, name="project_list"),
   
]
