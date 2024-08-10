from rest_framework import generics

from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
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
    search_fields = ['title', 'description', 'status', 'priority', 'owner__first_name', 'owner__last_name',]


class ToDoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority', 'due_date', 'created_at', 'updated_at', ]
    search_fields = ['title', 'description', 'status', 'priority', 'owner__first_name', 'owner__last_name',]

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user, is_archived=False)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()
    lookup_field = "id"


class ListArchiveToDoAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(owner=self.request.user, is_archived=True)
        return query


class ArchiveToDoAPIView(generics.UpdateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrAdmin,]
    queryset = ToDo.objects.all()
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status != "completed":
            return Response(
                {
                    "status": "error",
                    "message": 'Esta tarefa não pode ser arquivada. Não está "completa"'
                },
                status=status.HTTP_304_NOT_MODIFIED
            )

        task.is_archived = True
        task.save()
        serializer = self.serializer_class(task)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
