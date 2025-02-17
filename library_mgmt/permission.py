
from rest_framework.permissions import BasePermission,SAFE_METHODS
from rest_framework import serializers

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        else:
            if request.user.role == "admin":
                return True
            
            elif request.user.role == "member":
                if request.method in SAFE_METHODS:
                    return True
                else:
                    return False

        