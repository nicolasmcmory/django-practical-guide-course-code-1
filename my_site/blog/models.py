from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)


class Post(models.Model):

    title = models.CharField(max_length=200, default="no_title")
    slug = models.SlugField(default="", null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    content = models.TextField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="posts"
    )
    excerpt = models.TextField(max_length=100, null=True)
    image = models.CharField(null=True)
    published_date = models.DateField(null=True)
    caption = models.ManyToManyField(Tag, related_name="tags", null=True)

    # Overwrite save field to slugify
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = f"{slugify(self.title)}"
            return super().save(update_fields=["slug"])
        return super().save(*args, **kwargs)

    # Generate url by reverse lookup
    def get_absolute_url(self):
        return reverse("blog-post", args=[self.slug])
    
    def __str__(self):
        return self.title.capitalize()
