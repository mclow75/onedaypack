from django.contrib import admin
from .models import FastPoint


class FastPageAdmin(admin.ModelAdmin):
    verbose_name = "Точки"
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(FastPoint, FastPageAdmin)
