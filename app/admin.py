from django.contrib import admin
from .models import Tag, TodoItem

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
    )
    readonly_fields = ('timestamp',)