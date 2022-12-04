from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/todo_app/", include(('todo_app.urls', 'todo_app'), namespace='todo_app'))
]