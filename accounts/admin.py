from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone', 'bio')}),
    )
    list_display = UserAdmin.list_display + ('role', 'phone')
    list_filter = UserAdmin.list_filter + ('role',)

admin.site.register(User, CustomUserAdmin)
