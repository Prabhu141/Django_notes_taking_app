from django.contrib import admin
from .models import User, Note
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'user_name', 'is_staff', 'is_superuser', 'created_at', 'last_update')
    search_fields = ('email', 'user_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Dates', {'fields': ('created_at', 'last_update')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Note)
