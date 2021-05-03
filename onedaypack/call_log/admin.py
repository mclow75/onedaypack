from django.contrib import admin

from .models import Topic, Department, Contact, Advice, Note


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title')
    list_display_links = ('id', 'title')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title')
    search_field = ('title')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Contact)
admin.site.register(Advice)
admin.site.register(Note)
