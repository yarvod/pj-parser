from django.contrib import admin
from django.template.defaultfilters import truncatechars

from posts.models import RawPost, Channel, Vacancy


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'link')


@admin.register(RawPost)
class RawPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'channel',)
    list_filter = ('channel',)

    def short_text(self, obj):
        return truncatechars(obj.text, 35)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)
