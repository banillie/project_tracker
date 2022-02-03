import datetime
import os
from unittest import skip

from django.contrib.auth import get_user_model
from django.test import TestCase

from project_tracker.settings import ROOT_DIR
from .models import Engagement, EngagementType, EngagementWorkStream, EngagementTopic
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
    # def SetUp(self):
    #     wt_list = [
    #         'Lessons Learned',
    #         'Assurance',
    #         'Carbon',
    #         'Benefits',
    #         'Governance',
    #         'Risks and Issues',
    #         'Cost Estimating and Benchmarking',
    #         'Engineering',
    #         'Output Sec and Requirements',
    #         'Planning and Dependencies',
    #         'Portfolio',
    #         'Specialist Advice',
    #         'PDIP2']
    #
        # ws_list = [
        #     '24 Lessons Workshop',
        #     'Cultural Enquiry',
        #     'Red Team',
        #     'Management Case Review',
        #     'Benchmarking',
        #     'Assurance Review',
        #     'Resourcing & Recruitment',
        #     'Goverance',
        #     'SRO Letters']
    #
    #     for x in wt_list:
    #         EngagementType.objects.create(type=x)
    #
    #     for x in ws_list:
    #         EngagementWorkStream.objects.create(type=x)

    def setUp(self):
        # Stakeholders
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

        # PPDD data
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

        # Project data
        all_entries = {
            2: {
                "name": "Make a Big Bridge",
                "type": "Project",
                "abbreviation": "BIGBRIDGE",
                "governance": "Tier 1",
            },
            3: {
                "name": "Dig a Big Hole",
                "type": "Programme",
                "abbreviation": "BIGHOLE",
                "governance": "Tier 2",
            },
            4: {
                "name": "Make a Big Port",
                "type": "Portfolio",
                "abbreviation": "BIGPORT",
                "governance": "Tier 1",
            }
        }

        for x in all_entries:
            Project.objects.create(
                **all_entries[x],
            )

        # Engagement data
        type_list = [
            'Lessons Learned',
            'Assurance',
            'Carbon',
            'Benefits',
            'Governance',
            'Risks and Issues',
            'Cost Estimating and Benchmarking',
            'Engineering',
            'Output Sec and Requirements',
            'Planning and Dependencies',
            'Portfolio',
            'Specialist Advice',
            'PDIP2',
            '24 Lessons Workshop',
        ]

        for x in type_list:
            EngagementType.objects.create(type=x)

        ws_list = [
            '24 Lessons Workshop',
            'Cultural Enquiry',
            'Red Team',
            'Management Case Review',
            'Benchmarking',
            'Assurance Review',
            'Resourcing & Recruitment',
            'Goverance',
            'SRO Letters'
        ]

        for x in ws_list:
            EngagementWorkStream.objects.create(work_stream=x)

        a1 = Engagement(
                date=datetime.datetime(2021, 8, 25, 0, 0),
                summary="something something summary summary",
            )
        a1.save()
        a1.projects.add(Project.objects.get(id=1), Project.objects.get(id=2))
        a1.stakeholders.add(Stakeholder.objects.get(id=1), Stakeholder.objects.get(id=2))
        a1.ppdds.add(PPDD.objects.get(id=1), PPDD.objects.get(id=2))
        a1.engagement_types.add(EngagementType.objects.get(id=1), EngagementType.objects.get(id=5))
        a1.engagement_workstreams.add(EngagementWorkStream.objects.get(id=2))

        a2 = Engagement(
            date=datetime.datetime(2021, 9, 25, 0, 0),
            summary="something something summary summary",
        )
        a2.save()
        a2.projects.add(Project.objects.get(id=1), Project.objects.get(id=2))
        a2.stakeholders.add(Stakeholder.objects.get(id=1), Stakeholder.objects.get(id=2))
        a2.ppdds.add(PPDD.objects.get(id=1), PPDD.objects.get(id=2))
        a2.engagement_types.add(
            EngagementType.objects.get(type='Lessons Learned'),
            EngagementType.objects.get(type='Governance'),
            EngagementType.objects.get(type='24 Lessons Workshop'),  # test putting same object in
        )
        a2.engagement_workstreams.add(
            EngagementWorkStream.objects.get(work_stream='24 Lessons Workshop'),
            EngagementWorkStream.objects.get(work_stream='Assurance Review'),
        )

    def test_merge_worktype_with_workstream(self) -> None:
        for engagement in Engagement.objects.all():
            if engagement.engagement_types is not None:
                for type in engagement.engagement_types.all():
                    topic, created = EngagementTopic.objects.get_or_create(topic=type.type)
                    engagement.topics.add(EngagementTopic.objects.get(topic=topic))
            if engagement.engagement_workstreams is not None:
                for ws in engagement.engagement_workstreams.all():
                    topic, created = EngagementTopic.objects.get_or_create(topic=ws.work_stream)
                    engagement.topics.add(EngagementTopic.objects.get(topic=topic))

        a = Engagement.objects.get(pk=2)
        self.assertEqual(
            list(a.topics.values_list('topic', flat=True)),
            ['Lessons Learned', 'Governance', '24 Lessons Workshop', 'Assurance Review']
        )

    def test_stakeholder_data(self):
        a = Stakeholder.objects.get(pk=1)
        self.assertEqual(str(a.organisation), 'Org 1')

    def test_ppdd_data(self):
        self.assertEqual(PPDD.objects.count(), 3)

    def test_project_data(self):
        a = Project.objects.get(pk=1)
        self.assertEqual(a.type, 'Project')

    def test_engagement_data(self):
        a = Engagement.objects.get(pk=1)
        self.assertIsInstance(a.date, datetime.date)
        self.assertEqual(Engagement.objects.count(), 2)

    def test_engagement_filtering(self):
        a = Engagement.objects.filter(projects__id=1)
        self.assertEqual(a.count(), 2)
        b = Engagement.objects.filter(ppdds__id=1)
        self.assertEqual(b.count(), 2)
        c = Engagement.objects.filter(stakeholders__id=1)
        self.assertEqual(c.count(), 2)
        # return stakeholders that were in meeting where a project was discussed
        stake_qs = []
        for x in a.all().values('stakeholders').distinct():
            stake_qs.append(Stakeholder.objects.get(pk=x['stakeholders']))
        self.assertEqual(len(stake_qs), 2)
        # return projects discussed at meetings involving a stakeholder
        project_qs = []
        for x in c.all().values('projects').distinct():
            project_qs.append(Project.objects.get(pk=x['projects']))
        self.assertEqual(len(project_qs), 2)

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


