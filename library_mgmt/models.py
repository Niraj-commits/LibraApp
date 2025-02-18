from django.db import models
from core.models import User
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


class Reservation(models.Model):
    reserve_status = [('pending','pending'),('approved','approved'),('cancelled','cancelled')]
    
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
    book = models.ForeignKey(Book,on_delete = models.PROTECT,default=None)
    reservation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=50,choices=reserve_status,default='pending')
  
class BorrowingRecord(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
    book = models.ForeignKey(Book,on_delete = models.PROTECT,default=None)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.user} borrowed {self.book}"

class ReturnRecord(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
    book = models.ForeignKey(Book,on_delete = models.PROTECT,default=None)
    return_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} returned {self.book}"
