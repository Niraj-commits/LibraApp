
from rest_framework import serializers
from .models import *
from core.models import User

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']
    
    def create(self,validated_data):
        occurence = self.Meta.model.objects.filter(name = validated_data.get('name')).exists() #checking if the genre with same name exist
        
        if occurence:
            raise serializers.ValidationError("Genre with that name already exists.")
        
        genre = self.Meta.model(**validated_data)
        genre.save()
        return genre
    
    def update(self,instance,validated_data):
        occurence = self.Meta.model.objects.filter(name = validated_data.get('name')).exists() 
        if occurence:
            raise serializers.ValidationError("Member with that name already exists.")
        
        instance.name = validated_data.get('name')
        instance.save()
        return instance

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
        
        instance.title = validated_data.get('title')
        instance.genre = validated_data.get('genre')
        instance.is_available = validated_data.get('is_available')
        instance.author = validated_data.get('author')
        instance.save()
        return instance

class ReservationSerializer(serializers.ModelSerializer):
    
    book_name = serializers.StringRelatedField(source = "book")
    book_id = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.select_related('genre').all(),source = "book"
    )
    username = serializers.StringRelatedField(source = "user")
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),source = "user"
    )
    
    class Meta:
        model = Reservation
        fields = ['id','user_id','username','book_id','book_name','reservation_date','due_date','status']
    
    def create(self, validated_data):
        book = validated_data.get('book')
        status = validated_data.get('status')
        user = validated_data.get('user')
        reservation_date = validated_data.get('reservation_date')
        due_date = validated_data.get('due_date')
        occurence = Reservation.objects.filter(book = book,user = user).exists()
        
        if occurence:
            raise serializers.ValidationError({"Details":"You have already reserved this book"})
        
        if not book.is_available:
            raise serializers.ValidationError({"Details":"Sorry! Book is not available"})
        if status == "approved":#if book is available then make it unavailable
            book.is_available = False
            book.status = 'borrowed'
            book.save()
            BorrowingRecord.objects.create(
            book=book,user=user,borrow_date=reservation_date,due_date=due_date)
            
        reservation = Reservation.objects.create(**validated_data)
        return reservation
            
        
    def update(self,instance,validated_data):
        book = validated_data.get('book')
        status = validated_data.get('status')
        user = validated_data.get('user')
        due_date = validated_data.get('due_date')
        reservation_date = validated_data.get('reservation_date')
        occurence = Reservation.objects.filter(book = book,user = user).exists()
        
        if occurence:
            raise serializers.ValidationError({"Details":"You have already reserved this book"})
        
        if not book.is_available:
            raise serializers.ValidationError({"Details":"Sorry! Book is not available"})
        
        if status == "approved":#if book is available then make it unavailable
            book.is_available = False
            book.status = 'borrowed'
            book.save()
            BorrowingRecord.objects.create(
            book=book,user=user,borrow_date=reservation_date,due_date=due_date)
        instance.book = book
        instance.status = status
        instance.user = user
        instance.due_date = due_date
        instance.save()
        return instance
        
class BorrowingRecordSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source = 'user')
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),source = 'user'
    )
    book_name = serializers.StringRelatedField(source = 'book')
    class Meta:
        model = BorrowingRecord
        fields = ['id','user_id','username','book','book_name','borrow_date','due_date']
        
    def create(self,validated_data):    
        raise serializers.ValidationError({"Details":"Sorry Create Reservation Record For this"})
        
    def update(self,instance,validated_data):
        raise serializers.ValidationError({"Details":"Sorry Cannot Update The Details"})

class ReturnRecordSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source = 'user')
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),source = 'user'
    )
    book_name = serializers.StringRelatedField(source = 'book')
    class Meta:
        model = ReturnRecord
        fields = ['id','user_id','username','book','book_name','return_date']
        
    def create(self,validated_data):    
        book = validated_data.get('book') 
        if book is None:
            raise ValueError("Book object is not found.")
        if not book.is_available:
            book.is_available = True
            book.status = 'returned'
            book.save()
        
        else:
            raise serializers.ValidationError({"Details":"Book is already returned"})
        returnedBook = ReturnRecord.objects.create(**validated_data)
        return returnedBook
        
    def update(self,instance,validated_data):
        raise serializers.ValidationError({"Details":"Sorry Cannot Update The Details"})