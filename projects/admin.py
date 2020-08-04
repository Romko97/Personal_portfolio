from django.contrib import admin
from projects.models import Project, Technology

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "GitHub","image",)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id",)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)