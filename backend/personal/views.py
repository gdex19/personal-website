from django.shortcuts import render
from .models import Project

def index(request):
    return render(request, "personal/index.html", None)

def projects(request):
    project_list = Project.objects.all()
    return render(request, "personal/projects.html", context={"projects": project_list})
