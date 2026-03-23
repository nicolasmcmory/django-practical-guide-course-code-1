from django.contrib import admin
from .models import Post
from .models import Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "date")
    list_display = ("title", "date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "content")
    list_filter = ("user_name", "user_email")
    search_fields = ("user_name", "user_email", "content")

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
