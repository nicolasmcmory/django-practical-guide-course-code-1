from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to="media/", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
