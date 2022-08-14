from django.urls import path, include
from .views import home_view

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home')
]