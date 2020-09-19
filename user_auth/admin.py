from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, Group
from django.utils.translation import ugettext_lazy as _

from .models import User, Student, Teacher, StudentGroup

class StudentInline(admin.StackedInline):
    model = Student
    extra = 0

class TeacherInline(admin.StackedInline):
    model = Teacher
    extra = 0

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'address', 'dob')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name','last_name','phone_number','address','dob',),

        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'last_login')
    search_fields = ('email',)
    ordering = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined',)
    inlines = [StudentInline, TeacherInline]




admin.site.register(StudentGroup)
admin.site.unregister(Group)
