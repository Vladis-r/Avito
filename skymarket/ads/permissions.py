from rest_framework.permissions import BasePermission

from users.models import UserRoles


class UserPermission(BasePermission):
    message = "У вас нет разрешения на это действие"

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.author_id or request.user.role == UserRoles.ADMIN:
            return True
        return False




