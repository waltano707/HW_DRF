from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверяет, является ли пользователь Модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsStudent(permissions.BasePermission):
    """Проверяет, является ли пользователь Студентом"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
