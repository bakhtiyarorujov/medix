from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'birthday']
    list_display_links = ['full_name', 'email', 'phone', 'birthday']
