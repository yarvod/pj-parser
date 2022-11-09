from django.contrib import admin
from django.template.defaultfilters import truncatechars

from posts.models import RawPost, Vacancy, MessageEntity


class MessageEntityInline(admin.StackedInline):
    model = MessageEntity
    extra = 0


@admin.register(RawPost)
class RawPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'channel',)
    list_filter = ('channel',)
    search_fields = ('text',)
    inlines = (MessageEntityInline,)

    def short_text(self, obj):
        return truncatechars(obj.text, 35)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)
