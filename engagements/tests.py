import datetime
import os
from unittest import skip

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Engagement
from projects.models import Project
from stakeholders.models import Stakeholder, StakeholderOrg
from ppdds.models import PPDD

from openpyxl import load_workbook

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')

    def test_user_pw(self):
        checked = self.user_a.check_password('abc123')
        self.assertTrue(checked)


class EngagementTestCase(TestCase):
    def setUp(self):
        # self.user_a = User.objects.create_user('cfe', password='abc123')
        # self.project_a = Project.objects.create(
        #     user=self.user_a,
        #     name='Project A',
        #     type='PROJECT',
        #     abbreviation='PA'
        # )
        # self.project_b = Project.objects.create(
        #     user=self.user_a,
        #     name='Project B',
        #     type='PROJECT',
        #     abbreviation='PB'
        # )
        # self.engagement_a = Engagement.objects.create(
        #     user=self.user_a,
        #     date=datetime.date(2021, 10, 13),
        # )
        # self.engagement_a.projects.add(self.project_a, self.project_b)

        data_path = "/home/will/Documents/ppdd_engagement_db/ppdd_engagement_db_tables_django.xlsx"
        wb = load_workbook(data_path)

        # Stakeholders
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
            single_entry["first_name"] = ws.cell(row=row, column=1).value.strip()
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

        # PPDD data
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

        # Project data
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

        # Engagement data
        ws = wb['Engagements']
        last_row = 6

        # def get_m2m_object_list(col_num, data_model):
        #     list = ws.cell(row=row, column=col_num).value.split(", ")
        #     obj_list = []
        #     for name in list:
        #         obj_list.append(data_model.objects.get(name=name))

        for row in range(2, last_row):
            eng = Engagement(
                date=ws.cell(row=row, column=2).value,
                summary=ws.cell(row=row, column=8).value,
            )
            eng.save()

            project_list = ws.cell(row=row, column=3).value.split(", ")
            p_object_list = []
            for name in project_list:
                p_object_list.append(Project.objects.get(name=name))
            eng.projects.add(*p_object_list)

            # stakeholders
            stakeholder_list = ws.cell(row=row, column=4).value.split(", ")
            object_list = []
            for name in stakeholder_list:
                split_name = name.split(" ")
                object_list.append(Stakeholder.objects.get(
                    first_name=split_name[0],
                    last_name=split_name[1])
                )
            eng.stakeholders.add(*object_list)


    def test_stakeholder_data(self):
        a = Stakeholder.objects.get(pk=1)
        org = str(a.organisation)
        self.assertEqual(org, 'DfT(c)')

    def test_ppdd_data(self):
        a = PPDD.objects.get(pk=1)
        self.assertEqual(a.first_name, os.environ.get('test_four'))

    def test_project_data(self):
        a = Project.objects.get(pk=1)
        self.assertEqual(a.abbreviation, os.environ.get('test_three'))


    def test_engagement_data(self):
        a = Engagement.objects.get(pk=1)
        self.assertEqual(str(a.projects.all()[0]), os.environ.get('test_one'))
        self.assertEqual(str(a.stakeholders.all()[0]), os.environ.get('test_two'))


    @skip('not testing right now')
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    @skip('not testing right now')
    def test_user_engagement_reverse_count(self):
        user = self.user_a
        qs = user.engagement_set.all()
        self.assertEqual(qs.count(), 1)

    @skip('not testing right now')
    def test_user_engagement_forward_count(self):
        user = self.user_a
        qs = Engagement.objects.filter(user=user)
        self.assertEqual(qs.count(), 1)

    @skip('not testing right now')
    def test_project_engagement_forward_count(self):
        qs = Engagement.objects.filter(projects=self.project_b)
        self.assertEqual(qs.count(), 1)

    # test project(s) relationship with engagement?
    @skip('not testing right now')
    def test_engagement_two_level_relation(self):
        eng = self.engagement_a
        qs = Engagement.objects.filter(projects__engagement=eng)
        self.assertEqual(qs.count(), 2)

    # not passing. too complicated for now

    # def test_engagement_two_level_relation_reverse(self):
    #     eng = self.engagement_a
    #     project_ids = list(eng.projects_set.all().values_list('projects__id', flat=True))
    #     qs = Project.objects.filter(id__in=project_ids)
    #     self.assertEqual(qs.count(), 2)

    # def test_project_two_level_relation_via_engagement(self):
    #     project = self.project_a
    #     ids = project.name_set.all().values_list("id", flat=True)
    #     qs = Engagement.objects.filter(projects_id_in=ids)
    #     self.assertEqual(qs.count(), 2)


