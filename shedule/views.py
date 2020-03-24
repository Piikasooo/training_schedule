from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Task
from django.shortcuts import get_object_or_404
from .serializer import TaskSerializer


class TaskView(ViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(user)
        return Response(serializer.data)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action == ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = IsAdminUser,
        else:
            self.permission_classes = IsAuthenticated,
        return super().get_permissions()

