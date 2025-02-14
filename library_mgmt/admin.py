from django.contrib import admin
from .models import *
from .models import Member

# class MemberDisplay(admin.ModelAdmin):
#     list_display = ['user','phone','address']


class Borrow_Status(admin.TabularInline):
    model = Borrowed_Status
    extra = 0
    fields = ['book','status']

class Borrow(admin.ModelAdmin):
    list_display = ['member','book','borrow_date','due_date','return_date']
    inlines = [Borrow_Status]


# Register your models here.
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Genre)
admin.site.register(Borrowing_Record,Borrow)
admin.site.register(Reservation)
admin.site.register(Borrowed_Status)