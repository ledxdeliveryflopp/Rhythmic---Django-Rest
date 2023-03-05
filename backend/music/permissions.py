from rest_framework import permissions

from .models import Music


class IsUserTypeTrue(permissions.BasePermission):
    """Проверка на исполнителя"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type is True


class IsUserOwner(permissions.BasePermission):
    """Проверка на владение записи"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type is \
            True and Music.upload_by == request.user
