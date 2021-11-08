import os

from django.test import TestCase

from .models import Project
from project_tracker.settings import ROOT_DIR

from openpyxl import load_workbook

from django.utils.text import slugify
from .utils import slugify_instance_title


class ProjectTestCase(TestCase):

    def setUp(self):
        data_path = os.path.join(ROOT_DIR, 'project_tracker/data/project_tracker_data.xlsx')
        wb = load_workbook(data_path)
        ws = wb['Projects']
        all_entries = {}
        for row in range(2, ws.max_row + 1):
            single_entry = {}
            single_entry["name"] = ws.cell(row=row, column=2).value
            single_entry["type"] = ws.cell(row=row, column=1).value
            single_entry["abbreviation"] = ws.cell(row=row, column=3).value
            single_entry["governance"] = ws.cell(row=row, column=4).value
            all_entries[int(row)] = single_entry

        for x in all_entries:
            Project.objects.create(
                **all_entries[x],
            )

    def test_uploading_data(self):
        self.assertEqual(Project.objects.count(), 52)

