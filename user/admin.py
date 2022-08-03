from django.contrib import admin

from .models import (
    User,
)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'slug')
    list_display_links = ('id', 'username', 'email',)
    search_fields = ('id', 'username', 'email')
    fields = (
        'username', 'email',
        'is_staff', 'password', 'phone_number', 'code_mobile_operator',
        'created_at', 'time_zone'
    )
    readonly_fields = ['created_at']


admin.site.register(User, UsersAdmin)
