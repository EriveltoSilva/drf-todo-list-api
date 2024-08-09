from rest_framework import generics

from .models import ToDo
from .serializers import ToDoSerializer
from apps.accounts.permissions import IsOwnerOrAdmin, IsAdmin


class ToDoListAdminAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAdmin,]
    queryset = ToDo.objects.all()


class ToDoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()
    lookup_field = "id"
