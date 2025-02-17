from rest_framework import serializers
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','password','phone_number','address','role']

    def create(self,validated_data):
        user_occurence = self.Meta.model.objects.filter(username = validated_data.get('username')).exists() #checking if the user is already a member
        phone_occurence = self.Meta.model.objects.filter(phone_number = validated_data.get('phone_number')).exists()
        if user_occurence:
            raise serializers.ValidationError({"Details":"User already exist."})
        
        if phone_occurence:
            raise serializers.ValidationError({"Details":"Phone number already exist pick new number."})
            
        password = validated_data.pop('password') #To not show user password
        username = self.Meta.model.objects.create(**validated_data)
        username.set_password(password)
        username.save()
        return username