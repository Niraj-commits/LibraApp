from django.contrib import admin
from .models import User
from .forms import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUser(UserAdmin):
    model = User
    form = CustomUserForm
    add_form = CustomUserForm

    list_display = ['username', 'email', 'role']
    list_editable = ['role']
    list_filter = ['role']
    search_fields = ['username', 'email']
    ordering = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password1','password2','role')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1','password2', 'role'),
        }),
    )
admin.site.register(User,CustomUser)