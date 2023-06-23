from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from test_factory.factories import EngagementFactory

class EngagementURLTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.client = Client()
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_engagement_list_url(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('engagements:engagement-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagements/engagement_list.html')

    def test_engagement_create_url(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('engagements:engagement-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagements/engagement_create.html')

    def test_engagement_detail_url(self):
        engagement = EngagementFactory()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('engagements:engagement-detail', kwargs={"id": engagement.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagements/engagement_detail.html')

    def test_engagement_delete_url(self):
        engagement = EngagementFactory()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('engagements:engagement-delete', kwargs={"id": engagement.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagements/engagement_delete.html')

    def test_engagement_update_url(self):
        engagement = EngagementFactory()
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('engagements:engagement-update', kwargs={"id": engagement.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagements/engagement_create.html')

