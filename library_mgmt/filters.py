from django_filters import rest_framework as filter
from .models import *

class BookFilter(filter.FilterSet):
    class Meta:
        model = Book
        fields = [{
            'author':['exact'],
            'title':['exact'],
            'genre':['exact']
        },'is_available']