from django.contrib import admin

from .models import Topic, Entry, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "author", "entry", "date_added")


class EntryAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ("__str__", "topic", "date_added")


admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)
