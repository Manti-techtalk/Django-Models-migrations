from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField(max_length=1000)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
