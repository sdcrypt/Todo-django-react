from django.contrib import admin

# Register your models here.
from todo_app.models import Task, Note, Tag

class TaskAdmin(admin.ModelAdmin): 
    search_fields = ('title', )

class NoteAdmin(admin.ModelAdmin):
    search_fields = ('title', 'tag', )

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)