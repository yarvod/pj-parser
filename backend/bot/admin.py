from django.contrib import admin

from bot.models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'is_active')
