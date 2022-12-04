from rest_framework import serializers
from todo_app.models import Task, Note, Tag

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"