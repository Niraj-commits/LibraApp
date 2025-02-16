from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import *
from .pagination import CustomPagination
from rest_framework import filters
from rest_framework.response import Response
from .filter import *
from django_filters.rest_framework import DjangoFilterBackend 
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filter.DjangoFilterBackend]
    search_fields = ['genre','title','author']
    filterset_class = customFilter
    
    def destroy(self,request,pk):
        queryset = Book.objects.get(pk = pk)
        is_borrowed = BorrowingRecord.objects.filter(book = queryset).exists()
        is_reserved = Reservation.objects.filter(book = queryset).exists()
        if is_borrowed:
            raise serializers.ValidationError({"Details":"Book is Borrowed"})
        
        if is_reserved:
            raise serializers.ValidationError({"Details":"Book is Reserved"})
        
        else:
            queryset.delete()
            return Response({"Details":"Data has been deleted"})
        
class ReservationViewset(viewsets.ModelViewSet):
    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReturnRecordViewset(viewsets.ModelViewSet):
    
    queryset = ReturnRecord.objects.select_related('book','member').all()
    serializer_class = ReturnRecordSerializer