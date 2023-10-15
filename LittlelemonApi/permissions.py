from rest_framework import permissions

class ReadOnlyOrUnauthorized(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a member of the "Delivery crew" group
        user = request.user
        if user and user.groups.filter(name='Delivery crew').exists():
            # Allow GET requests (read-only)
            if request.method in permissions.SAFE_METHODS:
                return True
            # Deny POST, PUT, PATCH, DELETE requests
            return False
        # If the user is not a member of the "Delivery crew" group, consider them as customers
        # Allow GET requests (read-only) for customers
        if request.method in permissions.SAFE_METHODS:
            return True
        # Deny POST, PUT, PATCH, DELETE requests for customers
        return False
