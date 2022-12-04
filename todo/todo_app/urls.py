from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-details/<str:pk>/', views.task_detail_view, name="task-details"),
    path('task-create/', views.task_create, name="task-create"),
    path('task-detail/<str:pk>/', views.task_detail, name="task-detail"),
    
]