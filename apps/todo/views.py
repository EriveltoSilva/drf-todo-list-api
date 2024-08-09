from rest_framework import generics

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import ToDo
from .serializers import ToDoSerializer
from apps.accounts.permissions import IsOwnerOrAdmin, IsAdmin


class ToDoListAdminAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAdmin,]
    queryset = ToDo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'status', 'priority', 'due_date', 'created_at', 'updated_at', ]


class ToDoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority', 'due_date', 'created_at', 'updated_at', ]
    search_fields = ['title', 'description', 'status', 'priority', 'owner__first_name', 'owner__last_name',]

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()
    lookup_field = "id"
