from .models import User
from django_filters import rest_framework as filter

class UserFilter(filter.FilterSet):
    class Meta:
        model = User
        fields = {
            'phone_number':['exact'],
            'address':['exact'],
            'username':['exact'],
        }