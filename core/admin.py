from django.contrib import admin
from .models import User
# from .forms import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email','is_staff', 'password','role','phone_number','address')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','is_staff', 'password','role','phone_number','address'),
        }),
    )
    list_display = ['username', 'email','phone_number','role','address']
    list_editable = ['email','phone_number','role']
    list_filter = ['role']
    search_fields = ['username', 'email','role']

admin.site.register(User,CustomUser)
