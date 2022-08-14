from django.urls import path, include
from .views import (
    home_view,
    ProjectDetail,
    ProjectList,
)

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project-detail')
]