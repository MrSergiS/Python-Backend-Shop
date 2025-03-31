from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to allow only owners of an object to delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request method is DELETE
        if request.method == 'DELETE':
            return obj.owner == request.user
        return True
    