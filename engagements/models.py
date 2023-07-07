from django.conf import settings
from django.db import models
from django.urls import reverse
from projects.models import Project
from stakeholders.models import Stakeholder
from ppdds.models import PPDD
from django.db.models import Q

from simple_history.models import HistoricalRecords

User = settings.AUTH_USER_MODEL


# class EngagementQuerySet(models.QuerySet):
#     def search(self, query=None):
#         print(query)
#         a = EngagementTopic.objects.filter(engagement__topics__topic=query)
#         print(a)
#         if query is None or query == "":
#             return self.none()   # []
        # lookups = (
        #     Q(engagement__topics__topic__icontains=query)
            # | Q(governance__icontains=query)
            # | Q(abbreviation__icontains=query)
            # | Q(stage__icontains=query)
        # )
        # return self.filter(lookups)


# class EngagementManager(models.Manager):
#     def get_queryset(self):
#         return EngagementQuerySet(self.model, using=self._db)  # default db
#
#     def search(self, query=None):
#         return self.get_queryset().search(query=query)


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

    class Meta:
        ordering = ('topic',)


class Engagement(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    projects = models.ManyToManyField(Project)
    stakeholders = models.ManyToManyField(Stakeholder)
    ppdds = models.ManyToManyField(PPDD)
    topics = models.ManyToManyField(EngagementTopic)
    summary = models.TextField()
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse("engagements:engagement-detail", kwargs={"id": self.id})

    # def __str__(self):
    #     return self.date

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
