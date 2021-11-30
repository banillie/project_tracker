import os

from django.test import TestCase

from .models import Project
from project_tracker.settings import ROOT_DIR

from openpyxl import load_workbook

from django.utils.text import slugify
from .utils import slugify_instance_title


class ProjectTestCase(TestCase):

    def setUp(self):
        all_entries = {
            2: {
                "name": "Make a Big Bridge",
                "type": "Project",
                "abbreviation": "BIGBRIDGE",
                "governance": "Tier 1",
            },
            3: {
                "name": "Dig a Big Hole",
                "type": "Programme",
                "abbreviation": "BIGHOLE",
                "governance": "Tier 2",
            },
            4: {
                "name": "Make a Big Port",
                "type": "Portfolio",
                "abbreviation": "BIGPORT",
                "governance": "Tier 1",
            }
        }

        for x in all_entries:
            Project.objects.create(
                **all_entries[x],
            )

    def test_uploading_data(self):
        self.assertEqual(Project.objects.count(), 3)

    def test_filtering(self):
        a = Project.objects.search(query='PORT')
        b = Project.objects.search(query='1')
        c = Project.objects.search(query='Project')
        self.assertEqual(a.count(), 1)
        self.assertEqual(b.count(), 2)
        self.assertEqual(c.count(), 0)

