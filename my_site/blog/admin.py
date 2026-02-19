from django.contrib import admin
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author", "title","caption")
    

# Superuser: nicomain, password:1988
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)