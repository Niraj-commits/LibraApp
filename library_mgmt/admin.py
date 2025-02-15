from django.contrib import admin
from .models import *
from .models import Member

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_editable = ['name']
    search_fields = ['name']
    list_per_page = 10

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','genre','is_available','author']
    list_editable = ['title','genre','is_available','author']
    list_filter = ['genre','author']
    search_fields = ['title','author','genre']
    list_per_page = 10

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','address']
    list_editable = ['phone','address']
    list_filter = ['address']
    search_fields = ['user','address']
    list_per_page = 10

class BorrowAdmin(admin.ModelAdmin):
    list_display = ['member','book','borrow_date','due_date','return_date','status']
    list_editable = ['due_date','return_date','status']
    list_filter = ['status']
    search_fields = ['book','status']
    list_per_page = 10

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['member','book','reservation_date','status']
    list_editable = ['status']
    list_filter = ['status','member']
    search_fields = ['member','status']
    list_per_page = 10

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Borrowing_Record,BorrowAdmin)
admin.site.register(Reservation,ReservationAdmin)