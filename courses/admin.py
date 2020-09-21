from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Discipline

admin.sites.AdminSite.enable_nav_sidebar = False

admin.site.register(Discipline)


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['course_name', 'course_description']

