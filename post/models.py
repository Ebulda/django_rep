from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
