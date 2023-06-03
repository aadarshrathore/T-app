from rest_framework import viewsets
from .models import TodoItem, Tag
from .serializers import TodoItemSerializer, TagSerializer
from django.shortcuts import render
from django.http import HttpResponse
# create views

def home(request):
    return render(request,'index.html')
 
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

   