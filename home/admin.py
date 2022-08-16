from django.contrib import admin
from .models import (
    Category,
    Fact,
    News,
    PricingFeatures,
    Pricing,
    Project,
    Service,
    Solution,
    Team,
    Testimonial,
)

admin.site.register([
    Category,
    Fact,
    News,
    PricingFeatures,
    Pricing,
    Project,
    Service,
    Solution,
    Team,
    Testimonial,
])