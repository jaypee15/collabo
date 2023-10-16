from django.urls import path

from .views import (
    project_list,
    search
   
)

app_name = "projects"
urlpatterns = [
    path("", view=project_list, name="app"),
    path("search/", view=search, name="search"),

   
]
