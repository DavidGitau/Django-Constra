import imp
from django.shortcuts import render
from .models import (
    Fact, 
    Project,
)
from django.views.generic import ListView, DetailView

def home_view(request):
    context = {
        'facts': Fact.objects.all(),
        'object_list': Project.objects.all(),
    }
    return render(request, 'home/home.html', context)

def view_404(request):
    return render(request, 'other/404.html')

def about_view(request):
    return render(request, 'about/about.html')

def contact_view(request):
    return render(request, 'other/contact.html')

def faq_view(request):
    return render(request, 'other/faq.html')

def typography_view(request):
    return render(request, 'other/typography.html')

class CustomList(ListView):
    pass

class CustomDetail(DetailView):
    pass