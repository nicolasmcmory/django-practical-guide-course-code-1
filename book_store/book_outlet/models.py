from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, default="no_title")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title} Rating: {self.rating}"
