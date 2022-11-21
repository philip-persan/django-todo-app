from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'description', 'date_created', 'completed', 'date_completed'  # noqa
    list_display_links = 'id', 'user', 'description', 'date_created', 'completed'  # noqa
    list_filter = 'completed',
    list_per_page: int = 20
