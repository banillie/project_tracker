from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title


# not including user for this model as don't think its necessary
# not including timestamp and updated for this model as don't think its necessary
class PPDD(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, null=True, unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    tele_no = models.CharField(max_length=1000, blank=True, null=True)
    live = models.BooleanField(default=True)  # active?

    def get_absolute_url(self):
        return reverse("ppdds:detail", kwargs={"slug": self.slug})

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


def ppdd_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(ppdd_pre_save, sender=PPDD)


def ppdd_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(ppdd_post_save, sender=PPDD)