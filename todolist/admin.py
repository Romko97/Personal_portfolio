from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")

admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)