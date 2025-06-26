from typing import override
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrSharedReadOnly(BasePermission):
    @override
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.is_shared or obj.owner == request.user
        return obj.owner == request.user
