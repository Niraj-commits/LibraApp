from django_filters import rest_framework as filter
from .models import *

class genreFilter(filter.FilterSet):
    class Meta:
        model = Genre
        fields = {
            'name':['exact'],
        }
        
class bookFilter(filter.FilterSet):
    class Meta:
        model = Book
        fields = {
            'author':['exact'],
            'title':['exact'],
            'genre':['exact'],
            'is_available':['exact'],
        }

class memberFilter(filter.FilterSet):
    class Meta:
        model = Member
        fields = {
            'phone':['exact'],
            'address':['exact'],
        }

class reservationFilter(filter.FilterSet):
    class Meta:
        model = Reservation
        fields = {
            'member':['exact'],
            'book':['exact'],
            'reservation_date':['exact'],
            'status':['exact'],
        }

class borrowRecordFilter(filter.FilterSet):
    class Meta:
        model = BorrowingRecord
        fields = {
            'member':['exact'],
            'book':['exact'],
            'borrow_date':['exact']
        }

class returnRecordFilter(filter.FilterSet):
    class Meta:
        model = ReturnRecord
        fields = {
            'member':['exact'],
            'book':['exact'],
            'return_date':['exact']
        }

