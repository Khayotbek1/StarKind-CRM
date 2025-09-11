from rest_framework.permissions import BasePermission


class IsAdminOrManagerOrCaregiver(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.position in ["admin", "manager", "caregiver"]


