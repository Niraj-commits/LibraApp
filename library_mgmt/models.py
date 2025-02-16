from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    borrow_status = [('borrowed','borrowed'),('returned','returned'),('none','none')]
    
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre,on_delete=models.PROTECT,default=None,related_name="items")
    is_available = models.BooleanField(default=True)
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=borrow_status,default='none')
    
    def __str__(self):
        return self.title

class Member(models.Model):
    
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    user = models.ForeignKey('core.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Reservation(models.Model):
    reserve_status = [('pending','pending'),('approved','approved'),('cancelled','cancelled')]
    
    member = models.ForeignKey(Member,on_delete = models.PROTECT,default=None)
    book = models.ForeignKey(Book,on_delete = models.PROTECT,default=None)
    reservation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=reserve_status,default='pending')
  
class BorrowingRecord(models.Model):
    member = models.ForeignKey(Member,on_delete = models.PROTECT,default=None)
    book = models.ForeignKey(Book,on_delete = models.PROTECT,default=None)
    borrow_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.member} borrowed {self.book}"

class ReturnRecord(models.Model):
    member = models.ForeignKey(Member,on_delete = models.PROTECT,default=None)
    book = models.ForeignKey(Book,on_delete = models.PROTECT,default=None)
    return_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.member} returned {self.book}"
