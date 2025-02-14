from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import *
from .pagination import CustomPagination
from rest_framework import filters
from rest_framework.response import Response
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre','title','author']
    
    def destroy(self,request,pk):
        queryset = Book.objects.get(pk = pk)
        is_borrowed = Borrowing_Record.objects.filter(book = queryset).exists()
        is_reserved = Reservation.objects.filter(book = queryset).exists()
        if is_borrowed:
            raise serializers.ValidationError({"Details":"Book is Borrowed"})
        
        if is_borrowed:
            raise serializers.ValidationError({"Details":"Book is Reserved"})
        
        else:
            queryset.delete()
            return Response({"Details":"Data has been deleted"})