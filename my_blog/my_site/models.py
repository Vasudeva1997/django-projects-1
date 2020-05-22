from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image_file = models.ImageField(upload_to="post_pics")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("my_site:post_detail",kwargs={'pk':self.pk})

class Comment(models.Model):
    comment = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)

    def __str__(self):
        return self.author


