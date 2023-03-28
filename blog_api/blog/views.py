from django.shortcuts import render


from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializer


def index(request):
    return render(request,'index.html')

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCreate(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogUpdate(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

class BlogDelete(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

