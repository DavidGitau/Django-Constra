from django.shortcuts import render
from .models import Fact

def home_view(request):
    context = {
        'facts': Fact.objects.all()
    }
    return render(request, 'home/home.html', context)