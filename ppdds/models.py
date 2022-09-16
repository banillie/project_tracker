from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title

from simple_history.models import HistoricalRecords

User = settings.AUTH_USER_MODEL


class PPDDQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()   # []
        lookups = (
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(team__icontains=query)
            | Q(role__icontains=query)
        )
        return self.filter(lookups)


class PPDDManager(models.Manager):
    def get_queryset(self):
        return PPDDQuerySet(self.model, using=self._db)  # default db

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class PPDDDivison(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PPDD(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, null=True, unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    division = models.ForeignKey(PPDDDivison, on_delete=models.SET_NULL, null=True, blank=True)  # could make unique
    # true. Not essential at this time though.
    role = models.CharField(max_length=100, blank=True, null=True)
    tele_no = models.CharField(max_length=1000, blank=True, null=True)
    live = models.BooleanField(default=True)  # active?
    history = HistoricalRecords()

    objects = PPDDManager()

    def get_absolute_url(self):
        return reverse("ppdds:detail", kwargs={"slug": self.slug})

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ('first_name',)


def ppdd_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(ppdd_pre_save, sender=PPDD)


def ppdd_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(ppdd_post_save, sender=PPDD)