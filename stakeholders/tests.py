import os

from openpyxl import load_workbook

from django.test import TestCase
from .models import Stakeholder, StakeholderOrg
from project_tracker.settings import ROOT_DIR



class StakeholderTestCase(TestCase):

    def setUp(self) -> None:
        data_path = os.path.join(ROOT_DIR, 'project_tracker/data/project_tracker_data.xlsx')
        wb = load_workbook(data_path)
        ws = wb["Stakeholders"]
        org_list = []
        for row in range(2, ws.max_row + 1):
            org = ws.cell(row=row, column=3).value
            if org not in org_list:
                org_list.append(org)
            else:
                pass

        for x in org_list:
            StakeholderOrg.objects.create(org=x)

        all_entries = {}
        for row in range(2, ws.max_row + 1):
            single_entry = {}
            single_entry["first_name"] = ws.cell(row=row, column=1).value.strip()
            # using strip to tidy string whitespacing
            single_entry["last_name"] = ws.cell(row=row, column=2).value.strip()
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
        self.assertEqual(Stakeholder.objects.count(), 60)


    # testing required to handle stakeholders/ppdds with the same name.
    ## moved from project testing. More relevant to stakeholders.
    # def test_queryset_exists(self):
    #     qs = Project.objects.all()
    #     self.assertTrue(qs.exists())

    # def test_queryset_count(self):
    #     qs = Project.objects.all()
    #     self.assertEqual(qs.count(), self.number_of_articles)

    # def test_slug(self):
    #     obj = Project.objects.all().order_by("id").first()
    #     name = obj.name
    #     slug = obj.slug
    #     slugified_title = slugify(name)
    #     self.assertEqual(slug, slugified_title)

    # def test_unqiue_slug(self):
    #     qs = Project.objects.exclude(slug__iexact='hello-world')
    #     for obj in qs:
    #         name = obj.name
    #         slug = obj.slug
    #         slugified_title = slugify(name)
    #         self.assertNotEqual(slug, slugified_title)

    # def test_slugify_instance_title(self):
    #     obj = Project.objects.all().last()
    #     new_slugs = []
    #     for i in range(0, 25):
    #         instance = slugify_instance_title(obj, save=False)
    #         new_slugs.append(instance.slug)
    #     unique_slugs = list(set(new_slugs))
    #     self.assertEqual(len(new_slugs), len(unique_slugs))

    # def test_slugify_instance_title(self):
    #     slug_list = Project.objects.all().values_list('slug', flat=True)
    #     unique_slugs = list(set(slug_list))
    #     self.assertEqual(len(slug_list), len(unique_slugs))

    # def test_project_search_manager(self):
    #     qs = Project.objects.search(query='hello world')
    #     self.assertEqual(qs.count(), self.number_of_articles)

