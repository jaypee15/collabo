from django.urls import path

from .views import (
    project_list,
    search,
    project_detail
   
)

app_name = "projects"
urlpatterns = [
    path("", view=project_list, name="app"),
    path("search/", view=search, name="search"),
    path("project/<uuid:pk>", view=project_detail, name="project_detail")

   
]
