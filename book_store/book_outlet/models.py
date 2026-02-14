from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Data relations
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Dunder method, override
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


# id field is set automatically by Django
class Book(models.Model):
    title = models.CharField(max_length=50, default="no_title")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )
    # Relation field
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(
        default="", null=False, db_index=True
    )  # formats to "harry-potter-1" for example automatically

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # Dunder method, overrride
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author} Rating: {self.rating}"
