from django.db import models


class Category(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Category"


class Product(models.Model):
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(
        'post.Category', blank=True, related_name='category'
    )

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"


class Review(models.Model):
    product = models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

