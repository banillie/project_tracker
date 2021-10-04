from django.db import models
from django.forms import ModelForm
from django.urls import reverse

from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD
from multiselectfield import MultiSelectField

TYPE_CHOICES = (
    ('A', 'Assurance'),
    ('B', 'Benefits'),
    ('C', 'Carbon'),
    ('CC', 'Capability and Capacity'),
    ('CE', 'Cost Estimating and Benchmarking'),
    ('E', 'Engineering'),
    ('G', 'Goverance'),
    ('IT', 'Initial Triage'),
    ('LL', 'Lessons Learned'),
    ('OSR', 'Output Spec and Requirements'),
    ('PD', 'Planning and Dependencies'),
    ('PR', 'Portfolio Reporting'),
    ('RI', 'Risks and Issues')
)

WS_TYPE_CHOICES = (
    ('AR', 'Assurance'),
    ('BR', 'Business Case Review'),
    ('CE', 'Cultural Enquiry'),
    ('LL', 'Lessons Learned Workshop'),
    ('L24', '24 Lessons Workshop')
)

class EngagementType(models.Model):
    pass


class EngagementWorkStream(models.Model):
    pass


class Engagement(models.Model):
    date = models.DateField()
    projects = models.ManyToManyField(Project)
    stakeholders = models.ManyToManyField(Stakeholder)
    ppdds = models.ManyToManyField(PPDD)
    # Temporary TYPE_CHOICES drop down. Build EngagementType model?
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # Temporary WS_TYPE_CHOICES drop down. Build EngagementWsType model?
    ws_type = models.CharField(max_length=20, blank=True, null=True, choices=WS_TYPE_CHOICES)
    summary = models.TextField()
    follow_up_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("engagements:engagement-detail", kwargs={"id": self.id})


# build individual association tables
# # class StakeholderProjectEngagement(models.Model):
#     date = models.DateField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE )


# build one association table between projects, stakeholders, ppdd
# class Engagements(models.Model):
#     date = models.DateField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE)
#     ppdd = models.ForeignKey(PPDD, on_delete=models.CASCADE)
#     # this could also be a foreign key
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     # this could also be a foreign key
#     ws_type = models.CharField(max_length=20, blank=True, null=True, choices=WS_TYPE_CHOICES)
#     summary = models.TextField()
#     follow_up_date = models.DateField(blank=True, null=True)
