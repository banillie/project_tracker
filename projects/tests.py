from django.test import TestCase
from django.utils.text import slugify

from .models import Project
from .utils import slugify_instance_title

from openpyxl import load_workbook


class ProjectTestCase(TestCase):

    def setUp(self):
        data_path = "/home/will/Documents/ppdd_engagement_db/ppdd_engagement_db_tables_django.xlsx"
        wb = load_workbook(data_path)
        ws = wb['Projects']
        last_row = 54

        all_entries = {}
        for row in range(2, last_row):
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
        a = Project.objects.get(pk=1)
        print(a.name)

