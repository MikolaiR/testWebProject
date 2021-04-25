from django.contrib import admin

from todo.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["display_name", "create_date"]

    @staticmethod
    def display_name(obj):
        return obj
