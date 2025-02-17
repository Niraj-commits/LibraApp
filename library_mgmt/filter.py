from django_filters import rest_framework as filter
from .models import *
from core.models import User

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

class userFilter(filter.FilterSet):
    class Meta:
        model = User
        fields = {
            'phone_number':['exact'],
            'address':['exact'],
            'username':['exact'],
        }
class reservationFilter(filter.FilterSet):
    class Meta:
        model = Reservation
        fields = {
            'user':['exact'],
            'book':['exact'],
            'reservation_date':['exact'],
            'status':['exact'],
        }

class borrowRecordFilter(filter.FilterSet):
    class Meta:
        model = BorrowingRecord
        fields = {
            'user':['exact'],
            'book':['exact'],
            'borrow_date':['exact']
        }

class returnRecordFilter(filter.FilterSet):
    class Meta:
        model = ReturnRecord
        fields = {
            'user':['exact'],
            'book':['exact'],
            'return_date':['exact']
        }

