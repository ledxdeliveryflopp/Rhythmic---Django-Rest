from rest_framework import permissions


class IsUserTypeTrue(permissions.BasePermission):
    """Проверка на исполнителя"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type_user \
            == 'Исполнитель'


class IsUserOwner(permissions.BasePermission):
    """Проверка на владение обьектом"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.author == request.user


class IsUserUpdate(permissions.BasePermission):
    """Проверка на эдентичность пользователя"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.id == request.user.id
