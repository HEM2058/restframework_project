from rest_framework import permissions

class ReadOnlyOrUnauthorized(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user:
            if user.groups.filter(name='Delivery crew').exists():
                # Allow GET requests (read-only)
                if request.method in permissions.SAFE_METHODS:
                    return True
                # Deny POST, PUT, PATCH, DELETE requests
                return False
            elif user.groups.filter(name='Manager').exists():
                # Allow GET, POST, PUT, PATCH, DELETE requests for Managers
                return True

        # If the user is not in the "Delivery crew" or "Manager" group, consider them as customers
        # Allow GET requests (read-only) for customers
        if request.method in permissions.SAFE_METHODS:
            return True
        # Deny POST, PUT, PATCH, DELETE requests for customers
        return False
