from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics

from todo_app.models import Task, Note, Tag
from todo_app.serializers import TaskSerializer, NoteSerializer, TagSerializer
from django.http import HttpResponse
from django.template import loader



@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-detail/<str:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:pk>/",
        "Delete": "/task-delete/<str:pk>/"
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail_view(request, pk):
    task = Task.objects.filter(id=pk)
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PATCH', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteView(generics.ListCreateAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return self.queryset.filter(archive=False)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    






