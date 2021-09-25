from django.contrib import admin

from .models import Project, Dir

admin.site.register(Project)
admin.site.register(Dir)