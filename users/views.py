from rest_framework import permissions
from rest_framework import viewsets

from users.models import User
from users.serializer import UserSerializer


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owner of an user to edit it.
    """
    def has_permission(self, request, view):
        print(request.headers)
        if 'pk' not in view.kwargs:
            return False
        return str(request.user.id) == view.kwargs['pk']


class UserViewSet(viewsets.ModelViewSet):
    """
    Manipulate by users in the system.

    * Only admin users or owner are able to access this view.
    """
    permission_classes = [permissions.IsAdminUser | IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
