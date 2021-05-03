from django.contrib import admin

from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'edited_by')


admin.site.register(Notice, NoticeAdmin)
