from django.contrib import admin
from .models import ToDo


class ToDOAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'status', 'priority', 'owner', 'created_at', 'updated_at', ]
    list_display_links = ['title', 'due_date', 'status', 'priority', 'owner', 'created_at', 'updated_at', ]
    list_filter = ['status', 'priority', 'due_date', 'created_at', 'updated_at', ]
    search_fields = ['title', 'description', 'status',]
    list_per_page = 25
    ordering = ['-due_date', 'priority', '-created_at']


admin.site.register(ToDo, ToDOAdmin)
