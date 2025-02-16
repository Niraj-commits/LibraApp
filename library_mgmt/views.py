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
# Create your views here.

class GenreViewset(viewsets.ModelViewSet):
    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = genreFilter
    
    def destroy(self,request,pk):
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

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.select_related('user').all()
    serializer_class = MemberSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['phone','address']
    filterset_class = memberFilter
    
    def destroy(self,request,pk):
        queryset = Genre.objects.get(pk = pk)
        reservation_record = Book.objects.filter(member = queryset).exists()
        borrowing_record = BorrowingRecord.objects.filter(member = queryset).exists()
        return_record = ReturnRecord.objects.filter(member = queryset).exists()
        
        if reservation_record:
            raise serializers.ValidationError({"Details":"Reservation records exists for this member."},status = status.HTTP_226_IM_USED)
        if borrowing_record:
            raise serializers.ValidationError({"Details":"Borrowing records exists for this member."},status = status.HTTP_226_IM_USED)

        else:
            queryset.delete()
            return Response({"Details":"Member has been deleted"})
    
class ReservationViewset(viewsets.ModelViewSet):
    
    queryset = Reservation.objects.select_related('member','book').all()
    serializer_class = ReservationSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['book','reservation_date','status']
    filterset_class = reservationFilter
    
    def destroy(self,request,pk):
        queryset = Reservation.objects.get(pk = pk)
        
        if queryset.status != "approved":
            queryset.delete()
            return Response({"Reservation":"Data has been deleted"})
        
        else:
            raise serializers.ValidationError({"Details":"Reservation is already approved"},status= status.HTTP_226_IM_USED)

class BorrowingRecordViewset(viewsets.ModelViewSet):
    
    queryset = BorrowingRecord.objects.select_related('member','book').all()
    serializer_class = BorrowingRecordSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['member','book','borrow_date']
    filterset_class = borrowRecordFilter
    
    def destroy(self,request,pk):
        raise serializers.ValidationError({"Details":"Borrowing record cannot be deleted"},status = status.HTTP_401_UNAUTHORIZED)

class ReturnRecordViewset(viewsets.ModelViewSet):
    
    queryset = ReturnRecord.objects.select_related('book','member').all()
    serializer_class = ReturnRecordSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    search_fields = ['member','book','return_date']
    filterset_class = returnRecordFilter
    
    def destroy(self,request,pk):
        raise serializers.ValidationError({"Details":"Returned record cannot be deleted"},status = status.HTTP_401_UNAUTHORIZED)



