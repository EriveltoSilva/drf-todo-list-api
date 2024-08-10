"""api todo endpoints"""
from django.urls import path

from . import views

urlpatterns = [
    # ToDo endpoints
    path('', views.ToDoListCreateAPIView.as_view(), name="api-todo-list-create"),
    path('<uuid:id>/', views.ToDoRetrieveUpdateDestroyAPIView.as_view(), name="api-todo-retrieve-update-delete"),

    path('admin/', views.ToDoListAdminAPIView.as_view(), name="api-todo-list-admin"),
    path('archived/', views.ListArchiveToDoAPIView.as_view(), name="api-todo-archived-list"),
    path('archived/<uuid:id>/', views.ArchiveToDoAPIView.as_view(), name="api-todo-archive"),
]
