import unittest

from django.test import TestCase
from projects.models import Project
from test_factory.factories import ProjectFactory

class ProjectModelTest(TestCase):
    def test_get_absolute_url(self):
        project = ProjectFactory()
        expected_url = f"/projects/{project.slug}/"
        self.assertEqual(project.get_absolute_url(), expected_url)

    def test_get_update_url(self):
        project = ProjectFactory()
        expected_url = f"/projects/{project.slug}/update/"
        self.assertEqual(project.get_update_url(), expected_url)

    @unittest.skip('known bug. refactor coming')
    def test_get_hx_url(self):
        project = ProjectFactory()
        expected_url = f"/projects/{project.slug}/hx-detail/"
        self.assertEqual(project.get_hx_url(), expected_url)

    def test_str_representation(self):
        project = ProjectFactory(name="Test Project")
        self.assertEqual(str(project), "Test Project")

    def test_ordering(self):
        project1 = ProjectFactory(name="Project B")
        project2 = ProjectFactory(name="Project A")
        project3 = ProjectFactory(name="Project C")
        projects = Project.objects.all()
        self.assertEqual(projects[0], project2)
        self.assertEqual(projects[1], project1)
        self.assertEqual(projects[2], project3)

    def test_save_method(self):
        project = ProjectFactory()
        self.assertTrue(project.id)

    # Add more tests for other fields as needed

