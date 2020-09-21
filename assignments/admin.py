from django.contrib import admin

from .models import Assignment, AssignmentTaskFile, AssignmentAnswer


class AssignmentTaskFileInline(admin.TabularInline):
    model = AssignmentTaskFile
    raw_id_fields = ['assignment']
    extra = 1


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'discipline']
    inlines = [AssignmentTaskFileInline]


admin.site.register(AssignmentAnswer)
