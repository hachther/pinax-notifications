from django.contrib import admin

from .models import NoticeQueueBatch, NoticeSetting, NoticeType, NoticeStat
from .utils import load_media_defaults

NOTICE_MEDIA, NOTICE_MEDIA_DEFAULTS = load_media_defaults()


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "scoping", "send", 'key']


class NoticeStatAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "when"]
    list_filter = ('when', 'medium')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'notice_type__label')

    @admin.display(description='Medium', ordering='medium')
    def medium_label(self, obj):
        return NOTICE_MEDIA[obj.medium][1]


admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(NoticeSetting, NoticeSettingAdmin)
admin.site.register(NoticeStat, NoticeStatAdmin)
