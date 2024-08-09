from rest_framework import serializers

from .models import ToDo
from apps.accounts.serializers import UserSerializer


class ToDoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description', 'due_date', 'status', 'priority', 'owner', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at',)
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'due_date': {'required': True},
        }
