from rest_framework import permissions


class IsAuthenticatedOrObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь аутентифицированным
        if request.user.is_authenticated:
            # Проверяем, является ли пользователь владельцем объекта
            return obj == request.user
        return False
