from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'bio', 'first_name', 'last_name', 'email', 'profile_picture', 'facebook', 'twitter', 'instagram', 'youtube']

admin.site.register(CustomUser, CustomUserAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_draft', 'category', 'created_at']
admin.site.register(Blog, BlogAdmin)