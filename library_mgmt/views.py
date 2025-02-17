from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import *
from .pagination import CustomPagination
from rest_framework import filters
from rest_framework.response import Response
from .filter import *
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend 
from .permission import CustomPermission
# Create your views here.

class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all() #all objects of genre models
    serializer_class = GenreSerializer #serializer class to change dictionary to json objects
    pagination_class = CustomPagination #custom pagination class for paginating
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend] #filters for searching
    search_fields = ['name'] #field name for search
    filterset_class = genreFilter #custom filter class
    permission_classes = [CustomPermission]
    
    def destroy(self,request,pk): #for checking and deleting genre
        queryset = Genre.objects.get(pk = pk)
        genre_exist = Book.objects.filter(genre = queryset).exists()
        if genre_exist:
            raise serializers.ValidationError({"Details":"Genre is already used"},status = status.HTTP_226_IM_USED)

        else:
            queryset.delete()
            return Response({"Details":"Data has been deleted"})
    
class BookViewset(viewsets.ModelViewSet):
    
    queryset = Book.objects.select_related('genre').all()
    serializer_class = BookSerializers
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filter.DjangoFilterBackend]
    search_fields = ['genre','title','author']
    filterset_class = bookFilter
    permission_classes = [CustomPermission]
    
    def destroy(self,request,pk):
        queryset = Book.objects.get(pk = pk)
        is_borrowed = BorrowingRecord.objects.filter(book = queryset).exists()
        is_reserved = Reservation.objects.filter(book = queryset).exists()
        if is_borrowed:
            raise serializers.ValidationError({"Details":"Book is Borrowed"},status = status.HTTP_226_IM_USED)
        
        if is_reserved:
            raise serializers.ValidationError({"Details":"Book is Reserved"},status = status.HTTP_226_IM_USED)
        
        else:
            queryset.delete()
            return Response({"Details":"Data has been deleted"})


    
class ReservationViewset(viewsets.ModelViewSet):
    
    queryset = Reservation.objects.select_related('book').all()
    serializer_class = ReservationSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['book','reservation_date','status']
    filterset_class = reservationFilter
    permission_classes = [CustomPermission]
    
    def destroy(self,request,pk):
        queryset = Reservation.objects.get(pk = pk)
        
        if queryset.status != "approved":
            queryset.delete()
            return Response({"Reservation":"Data has been deleted"})
        
        else:
            raise serializers.ValidationError({"Details":"Reservation is already approved"},status= status.HTTP_226_IM_USED)

class BorrowingRecordViewset(viewsets.ModelViewSet):
    
    queryset = BorrowingRecord.objects.select_related('book').all()
    serializer_class = BorrowingRecordSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['user','book','borrow_date']
    filterset_class = borrowRecordFilter
    permission_classes = [CustomPermission]
    
    def destroy(self,request,pk):
        raise serializers.ValidationError({"Details":"Borrowing record cannot be deleted"},status = status.HTTP_401_UNAUTHORIZED)

class ReturnRecordViewset(viewsets.ModelViewSet):
    
    queryset = ReturnRecord.objects.select_related('book').all()
    serializer_class = ReturnRecordSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['user','book','return_date']
    filterset_class = returnRecordFilter
    permission_classes = [CustomPermission]
    
    def destroy(self,request,pk):
        raise serializers.ValidationError({"Details":"Returned record cannot be deleted"},status = status.HTTP_401_UNAUTHORIZED)



