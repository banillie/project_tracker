from django.conf import settings
from django.db import models
from django.urls import reverse
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD

User = settings.AUTH_USER_MODEL


class EngagementType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class EngagementWorkStream(models.Model):
    work_stream = models.CharField(max_length=50)

    def __str__(self):
        return self.work_stream


class EngagementTopic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic


class Engagement(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    projects = models.ManyToManyField(Project)
    stakeholders = models.ManyToManyField(Stakeholder)
    ppdds = models.ManyToManyField(PPDD)
    engagement_types = models.ManyToManyField(EngagementType)
    engagement_workstreams = models.ManyToManyField(EngagementWorkStream)
    topics = models.ManyToManyField(EngagementTopic)
    summary = models.TextField()
    # follow_up_date = models.DateField(blank=True, null=True)  # not sure required.

    def get_absolute_url(self):
        return reverse("engagements:engagement-detail", kwargs={"id": self.id})

    # def get_projects_children(self):
    #     return self.

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
