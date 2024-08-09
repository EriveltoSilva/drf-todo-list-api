import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDo(models.Model):
    STATUS_CHOICES = [("pending", "Pendente"), ("overdue", "Atrasado"), ("defer", "Adiado"), ("completed", "Concluído")]
    STATUS_PRIORITY = [('low', "Baixa"), ('middle', "Media"), ('high', "Alta"),]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    priority = models.CharField(max_length=20, choices=STATUS_PRIORITY, default=STATUS_PRIORITY[0][0])

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# 940 81 11 41
# Simple enough stuff so far - Coisas bem simples até aqui.
# So far, so good - Até agora tudo bem.
