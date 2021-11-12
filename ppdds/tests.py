import os
from django.test import TestCase

from .models import PPDD
from project_tracker.settings import ROOT_DIR

from openpyxl import load_workbook

from django.utils.text import slugify
from .utils import slugify_instance_title


class PPDDTestCast(TestCase):
    def setUp(self):
        data_path = os.path.join(ROOT_DIR, 'project_tracker/data/project_tracker_data.xlsx')
        wb = load_workbook(data_path)
        ws = wb['PPDDs']
        all_entries = {}
        for row in range(2, ws.max_row + 1):
            single_entry = {}
            single_entry["first_name"] = ws.cell(row=row, column=1).value.strip()
            single_entry["last_name"] = ws.cell(row=row, column=2).value.strip()
            single_entry["role"] = ws.cell(row=row, column=3).value
            single_entry["team"] = ws.cell(row=row, column=4).value
            single_entry["tele_no"] = ws.cell(row=row, column=5).value
            all_entries[int(row)] = single_entry

        for x in all_entries:
            PPDD.objects.create(
                **all_entries[x],
            )

    def test_uploading_data(self):
        self.assertEqual(PPDD.objects.count(), 16)

    def test_filtering(self):
        a = PPDD.objects.search(query='Field')
        self.assertEqual(a.count(), 1)

    ## slug testing to develop
    # def test_slug(self):
    #     obj = PPDD.objects.all().order_by("id").first()
    #     slug = obj.slug
    #     self.assertEqual(slug, 'jimmy-jones')
