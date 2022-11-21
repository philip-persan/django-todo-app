from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.is_superuser

    def has_permission(self, request, view):
        return super().has_permission(request, view)
