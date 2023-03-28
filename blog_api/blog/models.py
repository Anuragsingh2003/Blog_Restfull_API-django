from django.db import models


class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    location=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title