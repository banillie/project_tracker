from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from engagements.models import Engagement, EngagementTopic
from projects.models import Project
from stakeholders.models import Stakeholder, StakeholderOrg
from ppdds.models import PPDD


class EngagementModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='testuser')
        project = Project.objects.create(name='Test Project')
        stakeholder = Stakeholder.objects.create(
            first_name='Terry',
            last_name='Jacks',
            organisation=StakeholderOrg.objects.create(name='DfT(c)'),
        )
        ppdd = PPDD.objects.create(first_name='Jimmy', last_name='Jones')
        topic = EngagementTopic.objects.create(topic='Test Topic')

        Engagement.objects.create(
            user=user,
            date=date.today(),
            summary='Test Summary'
        )
        engagement = Engagement.objects.first()
        engagement.projects.add(project)
        engagement.stakeholders.add(stakeholder)
        engagement.ppdds.add(ppdd)
        engagement.topics.add(topic)

    def test_user_field(self):
        engagement = Engagement.objects.first()
        self.assertIsInstance(engagement.user, User)

    def test_date_field(self):
        engagement = Engagement.objects.first()
        self.assertIsInstance(engagement.date, date)

    def test_summary_field(self):
        engagement = Engagement.objects.first()
        self.assertIsInstance(engagement.summary, str)

    def test_projects_field(self):
        engagement = Engagement.objects.first()
        projects = engagement.projects.all()
        self.assertEqual(projects.count(), 1)

    def test_stakeholders_field(self):
        engagement = Engagement.objects.first()
        stakeholders = engagement.stakeholders.all()
        self.assertEqual(stakeholders.count(), 1)

    def test_ppdds_field(self):
        engagement = Engagement.objects.first()
        ppdds = engagement.ppdds.all()
        self.assertEqual(ppdds.count(), 1)

    def test_topics_field(self):
        engagement = Engagement.objects.first()
        topics = engagement.topics.all()
        self.assertEqual(topics.count(), 1)

    def test_history_field(self):
        engagement = Engagement.objects.first()
        self.assertEqual(engagement.history.count(), 0)

    def test_get_absolute_url(self):
        engagement = Engagement.objects.first()
        expected_url = f'/engagements/{engagement.id}/'
        self.assertEqual(engagement.get_absolute_url(), expected_url)
