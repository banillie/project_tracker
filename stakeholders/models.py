from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

from ppdds.utils import slugify_instance_title
from simple_history.models import HistoricalRecords

User = settings.AUTH_USER_MODEL


class StakeholderOrg(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DFTGroup(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class StakeholderQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()   # []
        lookups = (
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(organisation__name__icontains=query)
            | Q(dft_group__name__icontains=query)
        )
        return self.filter(lookups)


class StakeholderManager(models.Manager):
    def get_queryset(self):
        return StakeholderQuerySet(self.model, using=self._db)  # default db

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Stakeholder(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, null=True, unique=True)
    organisation = models.ForeignKey(StakeholderOrg, on_delete=models.SET_NULL, null=True)
    group = models.CharField(max_length=100, blank=True, null=True)
    dft_group = models.ForeignKey(DFTGroup, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    tele_no = models.CharField(max_length=1000, blank=True, null=True)
    live = models.BooleanField(default=True)
    my_dft_url = models.URLField(null=True, blank=True, unique=True)
    history = HistoricalRecords()

    objects = StakeholderManager()

    def get_absolute_url(self):
        # would be good to understand the reverse in more detail.
        return reverse("stakeholders:detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        # would be good to understand the reverse in more detail.
        return reverse("stakeholders:update", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.my_dft_url is None and self.organisation.name == 'DfT(c)':
            print(self.organisation)
            self.my_dft_url = "https://intranet.dft.gov.uk/users/" + slugify(self.first_name + ' ' + self.last_name)
        else:
            pass
        super().save(*args, **kwargs)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


def stakeholder_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(stakeholder_pre_save, sender=Stakeholder)


def stakeholder_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(stakeholder_post_save, sender=Stakeholder)