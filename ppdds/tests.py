from django.test import TestCase
from django.utils.text import slugify

from .models import PPDD
from .utils import slugify_instance_title
from openpyxl import load_workbook


class PPDDTestCast(TestCase):
    def setUp(self):
        data_path = "/home/will/Documents/ppdd_engagement_db/ppdd_engagement_db_tables_django.xlsx"
        wb = load_workbook(data_path)
        ws = wb['PPDDs']
        last_row = 17

        all_entries = {}
        for row in range(2, last_row):
            single_entry = {}
            single_entry["first_name"] = ws.cell(row=row, column=1).value
            single_entry["last_name"] = ws.cell(row=row, column=2).value
            single_entry["role"] = ws.cell(row=row, column=3).value
            single_entry["team"] = ws.cell(row=row, column=4).value
            single_entry["tele_no"] = ws.cell(row=row, column=5).value
            all_entries[int(row)] = single_entry

        for x in all_entries:
            PPDD.objects.create(
                **all_entries[x],
            )

    def test_uploading_data(self):
        a = PPDD.objects.get(pk=1)
        print(a)

    ## slug testing to develop
    # def test_slug(self):
    #     obj = PPDD.objects.all().order_by("id").first()
    #     slug = obj.slug
    #     self.assertEqual(slug, 'jimmy-jones')
