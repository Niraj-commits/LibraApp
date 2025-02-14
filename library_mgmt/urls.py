from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register(r'book',BookViewset,basename='book'),
urlpatterns = [
    path('',include(router.urls)),
]
