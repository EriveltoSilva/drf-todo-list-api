"""api todo endpoints"""
from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    # ToDo endpoints
    path('', views.ToDoListCreateAPIView.as_view(), name="list-create"),
    path('<uuid:id>/', views.ToDoRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-delete"),

    path('admin/', views.ToDoListAdminAPIView.as_view(), name="list-admin"),
    path('archived/', views.ListArchivedToDoAPIView.as_view(), name="list-archived"),
    path('archived/<uuid:id>/', views.ArchiveToDoAPIView.as_view(), name="retrieve-archived"),
]
