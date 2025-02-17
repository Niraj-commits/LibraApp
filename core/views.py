from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from library_mgmt.models import *
from .serializer import *
from rest_framework.authtoken.models import Token 
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .permission import CustomUserPermission
from rest_framework import filters
from .filter import UserFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import *
from drf_spectacular.utils import extend_schema_view,extend_schema,OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import action
# Create your views here.

class TokenViewset(APIView):
    
    @extend_schema(
        request= CreateUserSerializer,
        responses = {204:None},
        methods = ['POST']
    )
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username == None and password == None:
            raise serializers.ValidationError({"Details":"Sorry the fields cannot be empty"},status= status.HTTP_405_METHOD_NOT_ALLOWED)
        
        user_token = authenticate(username = username ,password = password)
        
        if user_token:
           token,_ =  Token.objects.get_or_create(user = user_token)
           return Response({
               "token":token.key,
               "user":username,
           })
        
        else:
            raise serializers.ValidationError({"Details":"Please enter valid credentials"})
        

class CreateUserViewset(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [CustomUserPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username','address','phone_number']
    filterset_class = UserFilter
    pagination_class = CustomPagination
    
    def destroy(self,request,pk):
        queryset = User.objects.get(pk = pk)
        reservation_record = Reservation.objects.filter(user = queryset).exists()
        borrowing_record = BorrowingRecord.objects.filter(user = queryset).exists()
        
        if reservation_record:
            raise serializers.ValidationError({"Details":"Reservation records exists for this User."},status = status.HTTP_226_IM_USED)
        if borrowing_record:
            raise serializers.ValidationError({"Details":"Borrowing records exists for this User."},status = status.HTTP_226_IM_USED)
        
        else:
            queryset.delete()
            return Response({"Details":"Member has been deleted"})