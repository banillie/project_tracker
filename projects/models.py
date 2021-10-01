from django.db import models
from django.urls import reverse


# Create your models here.

TYPE_CHOICES = [
    ("Project", "PROJECT"),
    ("Programme", "PROGRAMME"),
    ("Portfolio", "PORTFOLIO")
]


class Project(models.Model):
    # name must be unique
    name = models.CharField(max_length=120, null=False, unique=True)
    type = models.CharField(max_length=20, null=False, choices=TYPE_CHOICES)
    abbreviation = models.CharField(max_length=20, null=False)
    governance = models.CharField(max_length=20, blank=True, null=True)
    stage = models.CharField(max_length=20, blank=True, null=True)
    scope = models.TextField(max_length=200, blank=True, null=True)
    live = models.BooleanField(default=True, null=False)

    def get_absolute_url(self):
        return reverse("projects:project-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name


