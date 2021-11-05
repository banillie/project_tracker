from django.test import TestCase
from .models import Stakeholder, StakeholderOrg
# from data.test_data import stakeholder_data
from openpyxl import load_workbook


class StakeholderTestCase(TestCase):

    def setUp(self) -> None:
        data_path = "/home/will/Documents/ppdd_engagement_db/ppdd_engagement_db_tables_django.xlsx"
        wb = load_workbook(data_path)

        ws = wb["Stakeholders"]
        org_list = []
        last_row = 61
        for row in range(2, last_row):
            org = ws.cell(row=row, column=3).value
            if org not in org_list:
                org_list.append(org)
            else:
                pass

        for x in org_list:
            StakeholderOrg.objects.create(org=x)

        all_entries = {}
        for row in range(2, last_row):
            single_entry = {}
            single_entry["first_name"] = ws.cell(row=row, column=1).value
            single_entry["last_name"] = ws.cell(row=row, column=2).value
            org = ws.cell(row=row, column=3).value
            single_entry["organisation"] = StakeholderOrg.objects.get(org=org)
            single_entry["group"] = ws.cell(row=row, column=4).value
            single_entry["team"] = ws.cell(row=row, column=5).value
            single_entry["role"] = ws.cell(row=row, column=6).value
            single_entry["tele_no"] = ws.cell(row=row, column=7).value
            all_entries[int(row)] = single_entry

        for x in all_entries:
            Stakeholder.objects.create(
                **all_entries[x],
            )


    def test_uploading_data(self):
        a = Stakeholder.objects.get(pk=1)
        print(a.organisation)
