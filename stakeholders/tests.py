import os

from openpyxl import load_workbook

from django.test import TestCase
from .models import Stakeholder, StakeholderOrg
from project_tracker.settings import ROOT_DIR


class StakeholderTestCase(TestCase):
    def setUp(self) -> None:
        org_list = ['Org 1', 'Org 2']
        for x in org_list:
            StakeholderOrg.objects.create(org=x)

        all_entries = {
            2: {
                "first_name": "Andrew",
                "last_name": "Appiah",
                "organisation": StakeholderOrg.objects.get(org='Org 1'),
                "group": "RPE",
                "team": "RIS Client CIP Projects, Commercial &PDIP",
                "role": None,
                "tele_no": None,
            },
            3: {
                "first_name": "Albi",
                "last_name": "Luguiqi",
                "organisation": StakeholderOrg.objects.get(org='Org 2'),
                "group": None,
                "team": None,
                "role": None,
                "tele_no": None,
            },
        }

        for x in all_entries:
            Stakeholder.objects.create(
                **all_entries[x],
            )

    def test_uploading_data(self):
        self.assertEqual(Stakeholder.objects.count(), 2)

    def test_filtering(self):
        a = Stakeholder.objects.search(query='Org')
        self.assertEqual(a.count(), 2)

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

