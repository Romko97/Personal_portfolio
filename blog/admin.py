from django.contrib import admin
from blog.models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "last_modified",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "body", "created_on","post",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)