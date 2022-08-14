import imp
from django.shortcuts import render
from .models import (
    Fact, 
    Project,
)
from django.views.generic import ListView

def home_view(request):
    context = {
        'facts': Fact.objects.all(),
        'object_list': Project.objects.all(),
    }
    return render(request, 'home/home.html', context)

class ProjectList(ListView):
    model = Project
    template_name = 'project/project.html'