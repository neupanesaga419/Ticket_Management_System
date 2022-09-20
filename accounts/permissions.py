from rest_framework import permissions


class IsOnlyTicketUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print("Custom Permissions")
        if request.method in permissions.SAFE_METHODS:
            return obj.user.id == request.user.id or request.user.is_superuser
        
        
        return request.user.is_superuser
    
