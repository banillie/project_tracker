from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

TYPE_CHOICES = [
    ("Project", "PROJECT"),
    ("Programme", "PROGRAMME"),
    ("Portfolio", "PORTFOLIO")
]


class Project(models.Model):
    # name must be unique
    name = models.CharField(max_length=120, null=False, unique=True)
    slug = models.SlugField(blank=True, null=True)
    type = models.CharField(max_length=20, null=False, choices=TYPE_CHOICES)
    abbreviation = models.CharField(max_length=20, null=False)
    governance = models.CharField(max_length=20, blank=True, null=True)
    stage = models.CharField(max_length=20, blank=True, null=True)
    scope = models.TextField(max_length=200, blank=True, null=True)
    live = models.BooleanField(default=True, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("projects:project-detail", kwargs={"id": self.id})

    def save(self, *arg, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.name)
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.name


def slugify_instance_title(instance, save=False):
    slug = slugify(instance.name)
    qs = Project.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{qs.count() + 1}"
    instance.slug = slug
    if save:
        instance.save()


def project_pre_save(sender, instance, *args, **kwargs):
    print('pre-save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(project_pre_save, sender=Project)


def project_post_save(sender, instance, created, *args, **kwargs):
    print('post-save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(project_post_save, sender=Project)
