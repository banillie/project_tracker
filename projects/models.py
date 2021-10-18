from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.db.models import Q

from .utils import slugify_instance_title

TYPE_CHOICES = [
    ("Project", "PROJECT"),
    ("Programme", "PROGRAMME"),
    ("Portfolio", "PORTFOLIO")
]

User = settings.AUTH_USER_MODEL


class ProjectQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(name__icontains=query) | Q(scope__icontains=query)
        return self.filter(lookups)


class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Project(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120, null=False, unique=True)  # names are unique. title?
    slug = models.SlugField(blank=True, null=True)  # unique = true
    type = models.CharField(max_length=20, null=False, choices=TYPE_CHOICES)
    abbreviation = models.CharField(max_length=20, null=False)
    governance = models.CharField(max_length=20, blank=True, null=True)
    stage = models.CharField(max_length=20, blank=True, null=True)
    scope = models.TextField(max_length=200, blank=True, null=True)
    live = models.BooleanField(default=True, null=False)  # active?
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProjectManager()

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("projects:update", kwargs={"slug": self.slug})

    def get_hx_url(self):
        return reverse("projects:hx-detail", kwargs={"slug": self.slug})

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.name


def project_pre_save(sender, instance, *args, **kwargs):
    # print('pre-save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(project_pre_save, sender=Project)


def project_post_save(sender, instance, created, *args, **kwargs):
    # print('post-save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(project_post_save, sender=Project)
