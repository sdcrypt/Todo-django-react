from turtle import title
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    title =  models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date_published = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    archive = models.BooleanField(default=False, blank=True, null=True)
    pin_note = models.BooleanField(default=False)

    def __str__(self):
        return self.title