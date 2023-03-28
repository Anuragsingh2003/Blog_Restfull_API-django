from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_id', 'title', 'content','location','created_at', 'updated_at']
        read_only_fields = ['blog_id', 'created_at', 'updated_at']