from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
