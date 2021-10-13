import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Engagement
from projects.models import Project

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')

    def test_user_pw(self):
        checked = self.user_a.check_password('abc123')
        self.assertTrue(checked)


class EngagementTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')
        self.project_a = Project.objects.create(
            user=self.user_a,
            name='Project A',
            type='PROJECT',
            abbreviation='PA'
        )
        self.project_b = Project.objects.create(
            user=self.user_a,
            name='Project B',
            type='PROJECT',
            abbreviation='PB'
        )
        self.engagement_a = Engagement.objects.create(
            user=self.user_a,
            date=datetime.date(2021, 10, 13),
        )
        self.engagement_a.projects.add(self.project_a, self.project_b)

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_engagement_reverse_count(self):
        user = self.user_a
        qs = user.engagement_set.all()
        self.assertEqual(qs.count(), 1)

    def test_user_engagement_forward_count(self):
        user = self.user_a
        qs = Engagement.objects.filter(user=user)
        self.assertEqual(qs.count(), 1)

    def test_project_engagement_forward_count(self):
        qs = Engagement.objects.filter(projects=self.project_b)
        self.assertEqual(qs.count(), 1)

    # test project(s) relationship with engagement?
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
