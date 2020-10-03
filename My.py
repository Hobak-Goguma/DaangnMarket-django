from rest_framework.permissions import BasePermission
from rest_framework.permissions import AllowAny


class TokenAuthentication(BasePermission):
    def has_permission(self, request, view):
        if request.method == '':
            return True


permission_classes = (TokenAuthentication, )

permission_classes = [AllowAny]

@permission_classes([AllowAny])

def get_permissions(self):
    if self.action == 'retrieve':
        return [permission() for permission in [AllowAny]]
    else:
        return [permission() for permission in [IsAuthenticated]]