from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
	model = User
	list_display = ("username", "email", "first_name", "role", "is_staff")
	fieldsets = UserAdmin.fieldsets + (("Profile", {"fields": ("role", "profile_image")}),)
	add_fieldsets = UserAdmin.add_fieldsets + (("Profile", {"fields": ("role", "profile_image")}),)
