from django.contrib import admin
from .models import *

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_editable = ['name']
    search_fields = ['name']
    list_per_page = 10

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','genre','is_available','author','status']
    list_editable = ['title','genre','is_available','author']
    list_filter = ['genre','author','status']
    search_fields = ['title','author','genre','status']
    list_per_page = 10

class BorrowAdmin(admin.ModelAdmin):
    list_display = ['user','book','borrow_date']
    search_fields = ['book']
    list_per_page = 10

class ReturnAdmin(admin.ModelAdmin):
    list_display = ['user','book','return_date']
    search_fields = ['book']
    list_per_page = 10

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user','book','reservation_date','status']
    list_editable = ['status']
    list_filter = ['status','user']
    search_fields = ['user','status']
    list_per_page = 10

class BookReturnAdmin(admin.ModelAdmin):
    list_display = ['user','book','return_date']
    list_filter = ['book','user']
    search_fields = ['user','book']
    list_per_page = 10

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(BorrowingRecord,BorrowAdmin)
admin.site.register(ReturnRecord,ReturnAdmin)
admin.site.register(Reservation,ReservationAdmin)