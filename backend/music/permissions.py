from rest_framework import permissions
from .models import Music


class IsUserTypeTrue(permissions.BasePermission):
    """Проверка на исполнителя"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type_user \
            == 'Исполнитель'


class IsUserOwner(permissions.BasePermission):
    """Проверка на владение записи"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type_user \
            == 'Исполнитель' and obj.upload_by == request.user
