from rest_framework import permissions


class HaveTryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.attempts > 0:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
