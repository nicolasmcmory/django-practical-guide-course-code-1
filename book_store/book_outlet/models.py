from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)


class Address(models.Model):

    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.ManyToManyField(Country)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"


# Data relations
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    # Dunder method, override
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


# id field is set automatically by Django, one-to-many
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
    publised_country = models.ManyToManyField(Country)

    # Override default save conditionnally to avoid empty slugs (created using shell), fo Admin UI is already set up in params
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = f"{slugify(self.title)}"
            return super().save(update_fields=["slug"])
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # Dunder method, overrride
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author} Rating: {self.rating}"
