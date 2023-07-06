from django.test import TestCase
from django.urls import reverse, resolve

from test_factory.factories import ProjectFactory
from projects.urls import project_list_view

class ProjectTests(TestCase):
    def setUp(self):
        # self.user = User.objects.create_user(
        #     username="testuser", password="testpassword"
        # )
        # self.client.login(username="testuser", password="testpassword")
        self.project = ProjectFactory()

    def test_project_list_view(self):
        url = reverse("projects:list")
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, self.project.title)
        self.assertEquals(resolve(url).func, project_list_view)

    # def test_project_create_view(self):
    #     response = self.client.post(
    #         reverse("projects:create"), {"title": "New Project"}
    #     )
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(Project.objects.filter(title="New Project").exists())
    #
    # def test_project_update_view(self):
    #     response = self.client.post(
    #         reverse("projects:update", args=[self.project.slug]),
    #         {"title": "Updated Project"},
    #     )
    #     self.assertEqual(response.status_code, 302)
    #     self.project.refresh_from_db()
    #     self.assertEqual(self.project.title, "Updated Project")
    #
    # def test_project_delete_view(self):
    #     response = self.client.post(
    #         reverse("projects:delete", args=[self.project.slug])
    #     )
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Project.objects.filter(title=self.project.title).exists())
    #
    # def test_project_detail_view(self):
    #     response = self.client.get(reverse("projects:detail", args=[self.project.slug]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, self.project.title)
