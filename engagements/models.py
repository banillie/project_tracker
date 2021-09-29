from django.db import models
from django.forms import ModelForm
from django.urls import reverse


from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD

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


class Engagement(models.Model):
    date = models.DateField()
    # To come from projects Project model. One engagement can have many Projects entries.
    # what does on_delete do?
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # To come from stakeholders Stakeholder model. One engagement can have many Stakeholder entries.
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE)
    # To come from ppdds PPDD model. One engagement can have many PPDD entries.
    ppdd = models.ForeignKey(PPDD, on_delete=models.CASCADE)
    # Temporary TYPE_CHOICES drop down. Build EngagementType model?
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # Temporary WS_TYPE_CHOICES drop down. Build EngagementWsType model?
    ws_type = models.CharField(max_length=20, blank=True, null=True, choices=WS_TYPE_CHOICES)
    summary = models.TextField()
    follow_up_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("engagements:engagement-create", kwargs={"id": self.id})


class ProjectEngagement(models.Model):
    project = models.ManyToManyField(Project)
    engagement = models.ManyToManyField(Engagement)



