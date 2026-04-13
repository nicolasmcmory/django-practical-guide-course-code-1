from django.contrib import admin
from portal.models import User, Posts


# Admin classes
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "content", "author__first_name", "author__last_name")
    list_filter = ("created_at",)


# Registrations
admin.site.register(User, UserAdmin)
admin.site.register(Posts, PostAdmin)
