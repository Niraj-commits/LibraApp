
from rest_framework import serializers
from .models import *

class BookSerializers(serializers.ModelSerializer):
    genre_id = serializers.PrimaryKeyRelatedField(queryset = Genre.objects.all(),source = 'genre')
    genre = serializers.StringRelatedField()
    
    class Meta:
        model = Book
        fields = ['id','title','genre','genre_id','author','is_available']
        
    def create(self,validated_data):
        occurence = self.Meta.model.objects.filter(title = validated_data.get('title'),author = validated_data.get('author')).exists() #checking if the book with same name and author exist
        
        if occurence:
            raise serializers.ValidationError("Book With That Title Exists.")
        
        book = self.Meta.model(**validated_data)
        book.save()
        return book
    
    def update(self,instance,validated_data):
        occurence = self.Meta.model.objects.filter(title = validated_data.get('title'),author = validated_data.get('author')).exists()
        if occurence:
            raise serializers.ValidationError("Book With That Title Exists.")
        
        instance.__dict__.update(validated_data)
        instance.save()
        return instance
    

class ReservationSerializer(serializers.ModelSerializer):
    
    book_name = serializers.StringRelatedField(source = "book")
    book_id = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.all(),source = "book"
    )
    username = serializers.StringRelatedField(source = "member")
    member_id = serializers.PrimaryKeyRelatedField(
        queryset = Member.objects.all(),source = "member"
    )
    
    class Meta:
        model = Reservation
        fields = ['id','member_id','username','book_id','book_name','reservation_date','status']
    
    def create(self, validated_data):
        book = validated_data.get('book')
        status = validated_data.get('status')
        member = validated_data.get('member')
        
        if book.is_available and status == "approved": #if book is available then make it unavailable
            book.is_available = False
            book.status = 'borrowed'
            book.save()
            
        elif not book.is_available:
            raise serializers.ValidationError("Sorry! Book is not available")
        
        reservation = Reservation.objects.create(**validated_data)
    
        BorrowingRecord.objects.create(
            book=book,member=member,borrow_date=reservation.reservation_date)
        return reservation
        
    def update(self,instance,validated_data):
        book = validated_data.get('book')
        status = validated_data.get('status')
        if book.is_available and status == "approved": #To Check if book is available and reservation is approved
            book.is_available = False
            book.save()

        elif not book.is_available:
            raise serializers.ValidationError("Sorry! Book is not available")
        
        instance.__dict__.update(validated_data) #using __dict__(existing object's attribute) and changing to (validated_data)
        return instance

class ReturnRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnRecord
        fields = ['id','member','book','return_date']
        
    def create(self,validated_data):
        book = validated_data.get('book')
        book.is_available = True
        book.status = 'returned'
        book.save()
        returnedBook = ReturnRecord.objects.create(**validated_data)
        return returnedBook