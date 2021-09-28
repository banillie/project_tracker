from django.db import models
from django.urls import reverse


class PPDD(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    # team = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    tele_no = models.CharField(max_length=1000, blank=True, null=True)
    live = models.BooleanField(default=True)

    def get_absolute_url(self):
        # would be good to understand the reverse in more detail.
        return reverse("ppdds:ppdd-detail", kwargs={"id": self.id})
