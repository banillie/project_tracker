from django.db import models
from django.forms import ModelForm
from django.urls import reverse

from projects.models import Project


class Engagement(models.Model):
    date = models.DateField()
    summary = models.TextField()
    follow_up_date = models.DateField()

    def get_absolute_url(self):
        return reverse("engagements:engagement-create", kwargs={"id": self.id})


class ProjectEngagement(models.Model):
    project = models.ManyToManyField(Project)
    engagement = models.ManyToManyField(Engagement)
