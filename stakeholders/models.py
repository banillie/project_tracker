from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from ppdds.utils import slugify_instance_title


class StakeholderOrg(models.Model):
    org = models.CharField(max_length=30)

    def __str__(self):
        return self.org


class Stakeholder(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    slug = slug = models.SlugField(blank=True, null=True, unique=True)
    # need to understand on_delete better
    organisation = models.ForeignKey(StakeholderOrg, on_delete=models.CASCADE) # null=False
    group = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    tele_no = models.CharField(max_length=1000, blank=True, null=True)
    live = models.BooleanField(default=True)

    def get_absolute_url(self):
        # would be good to understand the reverse in more detail.
        return reverse("stakeholders:detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        # would be good to understand the reverse in more detail.
        return reverse("stakeholders:update", kwargs={"slug": self.slug})

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)

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