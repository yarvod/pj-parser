import requests
from django.conf import settings
from django.contrib import admin
from django.template.defaultfilters import truncatechars

from posts.models import RawPost, Vacancy, MessageEntity, News
from posts.serializers import NewsSerializer


class MessageEntityInline(admin.StackedInline):
    model = MessageEntity
    extra = 0


class NewsInline(admin.StackedInline):
    model = News
    extra = 0


@admin.register(RawPost)
class RawPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'channel', 'created')
    list_filter = ('channel',)
    search_fields = ('text',)
    inlines = (NewsInline, MessageEntityInline)
    actions = ('transfer2news',)

    def short_text(self, obj):
        return truncatechars(obj.text, 35)

    short_text.short_description = 'Текст'

    @admin.action(description='Перевести в новость')
    def transfer2news(self, request, queryset):
        for post in queryset:
            News.objects.create(
                text=post.text,
                date=post.created,
                raw_post=post
            )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'date')
    actions = ('publish',)

    def short_text(self, obj):
        return truncatechars(obj.text, 35)

    short_text.short_description = 'Текст'

    @admin.action(description='Опубликовать')
    def publish(self, request, queryset):
        for post in queryset:
            data = NewsSerializer(post).data
            requests.post(
                url=settings.NEWS_URL,
                auth=(settings.PHYSTECHJOB_USER, settings.PHYSTECHJOB_PWD),
                json=data
            )
