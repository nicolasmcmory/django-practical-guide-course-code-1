from django.contrib import admin
from portal.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    
admin.site.register(User, UserAdmin)
