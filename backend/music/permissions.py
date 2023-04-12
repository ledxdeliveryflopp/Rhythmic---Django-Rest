from rest_framework import permissions


class IsUserTypeTrue(permissions.BasePermission):
    """Проверка на исполнителя"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type_user \
            == 'Исполнитель'


class IsUserTrackOwner(permissions.BasePermission):
    """Проверка на владение треком"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type_user \
            == 'Исполнитель' and obj.author == request.user


class IsUserAlbumOwner(permissions.BasePermission):
    """Проверка на владение альбома"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and request.user.type_user \
            == 'Исполнитель' and obj.author == request.user
