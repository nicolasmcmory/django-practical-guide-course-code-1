from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "date")
    list_display = ("title", "date")


admin.site.register(Post, PostAdmin)
