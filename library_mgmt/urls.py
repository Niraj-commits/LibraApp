from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register(r'book',BookViewset,basename='book'),
router.register(r'genre',GenreViewset,basename='genre'),
router.register(r'member',MemberViewset,basename='member'),
router.register(r'reservation',ReservationViewset,basename='reservation'),
router.register(r'borrow_book',BorrowingRecordViewset,basename='borrow_book'),
router.register(r'return_book',ReturnRecordViewset,basename='return_book'),
urlpatterns = [
    path('',include(router.urls)),
]
