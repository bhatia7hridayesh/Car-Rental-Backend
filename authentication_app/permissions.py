from rest_framework.permissions import BasePermission


class IsUser(BasePermission):  
    def has_permission(self, request, view):  
        return request.user.user_type == "User" 

class IsAgency(BasePermission):  
    def has_permission(self, request, view): 
        return request.user.user_type == "Agency" 
