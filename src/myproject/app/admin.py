# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from .models import User, Course, Rating

class UserAdmin(BaseUserAdmin):
    list_display = ('mssv', 'name', 'email', 'is_staff', 'is_active')
    search_fields = ('mssv', 'name', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('mssv',)
    fieldsets = (
        (None, {'fields': ('mssv', 'password')}),
        ('Personal info', {'fields': ('name', 'email', 'avatar', 'raw_password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
    )
    filter_horizontal = ('user_permissions',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('ma_mon_hoc', 'ten_mon_hoc', 'so_tin_chi', 'ten_giang_vien', 'so_luong_cmt')
    search_fields = ('ma_mon_hoc', 'ten_mon_hoc', 'ten_giang_vien')
    ordering = ('ma_mon_hoc',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('mssv', 'name', 'course', 'cau1', 'cau2', 'cau3', 'cau4')
    search_fields = ('mssv', 'name', 'course__ten_mon_hoc')
    ordering = ('course', 'mssv')

admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Rating, RatingAdmin)
