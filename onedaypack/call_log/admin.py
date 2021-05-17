from django.contrib import admin

from .models import Topic, Department, Contact, Advice, Note


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title')
    list_display_links = ('id', 'title')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title')
    search_field = ('title')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'sni14', 'fio', 'edited_by', 'updated_at')
    list_display_links = ('id', 'sni14', 'fio')
    ordering = ['updated_at']


class AdviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'duration', 'edited_by', 'updated_at')
    list_display_links = ('id', 'edited_by', 'updated_at')
    ordering = ['-updated_at']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Advice, AdviceAdmin)
admin.site.register(Note)
