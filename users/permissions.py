from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User

class Permition(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated and request.user.is_employee
    

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_employee or obj == request.user
