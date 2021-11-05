from django.test import TestCase
from django.utils.text import slugify

from .models import Project
from .utils import slugify_instance_title

from openpyxl import load_workbook


class ProjectTestCase(TestCase):

    def setUp(self):
        # self.number_of_articles = 500
        # for i in range(0, self.number_of_articles):
        #     Project.objects.create(
        #         name='Hello World',
        #         type='Project',
        #         abbreviation='HE'
        #     )

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
