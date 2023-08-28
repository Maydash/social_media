from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet


class UserNetAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ( ('Personal info'), {'fields': ('first_name', 'last_name', 'middle_name', 'email')}),
        ( ('permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ( ('Important dates'), {'fields': ('last_login', 'date_joined')}),
        ( ('Info'), {'fields': ('phone', 'avatar', 'gender')}),
    )


admin.site.register(UserNet, UserNetAdmin)
