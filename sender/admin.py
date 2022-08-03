from django.contrib import admin
from .models import (
    Mailing,
    TextMessage,
)


class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_to_send', 'end_time', 'launch_time')
    list_display_links = ('id', 'text_to_send',)
    search_fields = ('id', 'text_to_send')


class TextMessageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_mailing', 'mailing_name',
        'status',
    )
    list_display_links = ('id', 'user_mailing', 'mailing_name')
    search_fields = ('id', 'user_mailing', 'mailing_name')


admin.site.register(Mailing, MailingAdmin)
admin.site.register(TextMessage, TextMessageAdmin)
