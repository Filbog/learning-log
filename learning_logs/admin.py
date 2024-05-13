from django.contrib import admin

from .models import Topic, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "topic", "date_added")


admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
