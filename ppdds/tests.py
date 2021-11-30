import os
from django.test import TestCase

from .models import PPDD
from project_tracker.settings import ROOT_DIR

from openpyxl import load_workbook

from django.utils.text import slugify
from .utils import slugify_instance_title


class PPDDTestCast(TestCase):
    def setUp(self):
        all_entries = {
            2: {
                "first_name": "Micky",
                "last_name": "Mouse",
                "role": "Entertainer",
                "team": "Disney",
                "tele_no": None,
            },
            3: {
                "first_name": "James",
                "last_name": "Brown",
                "role": "Musician",
                "team": "Funky",
                "tele_no": None,
            },
            4: {
                "first_name": "David",
                "last_name": "Blaine",
                "role": "Magician",
                "team": "Astonish",
                "tele_no": None,
            }
        }

        for x in all_entries:
            PPDD.objects.create(
                **all_entries[x],
            )

    def test_uploading_data(self):
        self.assertEqual(PPDD.objects.count(), 3)

    def test_filtering(self):
        a = PPDD.objects.search(query='Blaine')
        self.assertEqual(a.count(), 1)

    ## slug testing to develop
    # def test_slug(self):
    #     obj = PPDD.objects.all().order_by("id").first()
    #     slug = obj.slug
    #     self.assertEqual(slug, 'jimmy-jones')
