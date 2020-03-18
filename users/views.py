from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

from .serializer import UserSerialiser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerialiser

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = AllowAny
        else:
            self.permission_classes = IsAuthenticated, IsAdminUser
        return super().get_permissions()
