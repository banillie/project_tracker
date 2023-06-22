from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
# from django.utils.decorators import login_required
# from engagements.views import engagement_list_view, engagement_create_view, engagement_detail_view, engagement_delete_view, \
#     EngagementUpdateView

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
        self.assertTemplateUsed(response, 'engagement_create.html')

    def test_engagement_detail_url(self):
        self.client.login(username='testuser', password='testpassword')
        engagement_id = 1  # Replace with a valid engagement ID
        response = self.client.get(reverse('engagements:engagement-detail', args=[engagement_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagement_detail.html')

    def test_engagement_delete_url(self):
        engagement_id = 1  # Replace with a valid engagement ID
        response = self.client.get(reverse('engagements:engagement-delete', args=[engagement_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagement_delete.html')

    def test_engagement_update_url(self):
        engagement_id = 1  # Replace with a valid engagement ID
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('engagements:engagement-update', args=[engagement_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'engagement_update.html')

