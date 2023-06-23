from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date

from test_factory.factories import EngagementFactory
# from engagements.models import Engagement, EngagementTopic
from projects.models import Project
from stakeholders.models import Stakeholder, StakeholderOrg
from ppdds.models import PPDD


class EngagementModelTest(TestCase):
    # This causes a crash. don't know why?
    # @classmethod
    # def setUpTestData(cls):
    #     super().setUpClass()
    #     cls.engagement = EngagementFactory()

    def test_user_field(self):
        engagement = EngagementFactory()
        self.assertIsInstance(engagement.user, User)

    def test_date_field(self):
        engagement = EngagementFactory()
        self.assertIsInstance(engagement.date, date)

    def test_summary_field(self):
        engagement = EngagementFactory()
        self.assertIsInstance(engagement.summary, str)

    def test_projects_field(self):
        engagement = EngagementFactory()
        projects = engagement.projects.all()
        self.assertEqual(projects.count(), 1)

    def test_stakeholders_field(self):
        engagement = EngagementFactory()
        stakeholders = engagement.stakeholders.all()
        self.assertEqual(stakeholders.count(), 1)

    def test_ppdds_field(self):
        engagement = EngagementFactory()
        ppdds = engagement.ppdds.all()
        self.assertEqual(ppdds.count(), 1)

    def test_topics_field(self):
        engagement = EngagementFactory()
        topics = engagement.topics.all()
        self.assertEqual(topics.count(), 1)

    def test_get_absolute_url(self):
        engagement = EngagementFactory()
        expected_url = f'/engagements/{engagement.id}/'
        self.assertEqual(engagement.get_absolute_url(), expected_url)
