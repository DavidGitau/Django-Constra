from django.contrib import admin
from .models import (
    Category,
    Fact,
    Project,
)

admin.site.register([Category, Fact, Project])