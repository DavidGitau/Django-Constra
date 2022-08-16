from django.urls import path, include
from .views import (
    home_view,
    about_view,
    contact_view,
    faq_view,
    typography_view,
    view_404,
    CustomDetail,
    CustomList,
)
from .models import (
    News,
    Pricing,
    Project,
    Service,
    Team,
    Testimonial,
)

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('404/', view_404, name='404'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('faq/', faq_view, name='faq'),
    path('typography/', typography_view, name='typography'),

    # News urls
    path(
        'news-right/', 
        CustomList.as_view(
            model = News,
            template_name = 'news/news-right.html'
        ), 
        name='news-right'
        ),
    path(
        'news-left/', 
        CustomList.as_view(
            model = News,
            template_name = 'news/news-left.html'
        ), 
        name='news-left'
        ),
    path(
        'news/<int:pk>/', 
        CustomDetail.as_view(
            model = News,
            template_name = 'news/detail.html'
        ), 
        name='news-detail'
        ),

    # Pricing url
    path(
        'pricing/', 
        CustomList.as_view(
            model = Pricing,
            template_name = 'other/pricing.html'
        ), 
        name='pricing'
        ),
    
    # Project urls
    path(
        'projects/', 
        CustomList.as_view(
            model = Project,
            template_name = 'project/project.html'
        ), 
        name='project'
        ),
    path(
        'project/<int:pk>/', 
        CustomDetail.as_view(
            model = Project,
            template_name = 'project/detail.html'
        ), 
        name='project-detail'
        ),

    # Service urls
    path(
        'service/', 
        CustomList.as_view(
            model = Service,
            template_name = 'service/service.html'
        ), 
        name='service'
        ),
    path(
        'service/<int:pk>/', 
        CustomDetail.as_view(
            model = Service,
            template_name = 'service/detail.html'
        ), 
        name='service-detail'
        ),

    # Team url
    path(
        'team/', 
        CustomList.as_view(
            model = Team,
            template_name = 'team/team.html'
        ), 
        name='team'
        ),

    # testimonial url
    path(
        'testimonial/', 
        CustomList.as_view(
            model = Testimonial,
            template_name = 'other/testimonial.html'
        ), 
        name='testimonial'
        ),
]