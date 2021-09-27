from django.db import models

TYPE_CHOICES = [
    ('DfT', 'DFT'),
    ('HS2 LTD', 'HS2 LTD'),
    ('Highways England', 'HIGHWAYS ENGLAND'),
    ('MCA', 'MCA')
]


class Stakeholder(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    organisation = models.CharField(max_length=60, null=False, choices=TYPE_CHOICES)
    group = models.CharField(max_length=100)
    team = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    tele_no = models.CharField(max_length=1000, blank=True, null=True)
    live = models.BooleanField(default=True)
