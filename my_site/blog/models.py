from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Post(models.Model):

    title = models.CharField(max_length=200, default="no_title")
    slug = models.SlugField(default="", null=False, db_index=True)
    # content = models.TextField()
    content = models.TextField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="posts"
    )
    # excerpt = models.CharField()
    # img_name = models.ImageField()
    # published_date = models.DateField()

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

    # Get recent posts with a default count of 3
    """ def get_recent_posts(self, count: int = 3) -> dict:
        return dict(
            sorted(
                self.posts.items(),
                key=lambda item: item[1]["published_date"],
                reverse=True,
            )[:count]
        ) """


# class Tag(models.Model):
#     caption = ''
