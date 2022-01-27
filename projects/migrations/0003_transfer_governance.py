# Generated by Django 3.2 on 2022-01-24 10:55

from django.db import migrations


def link_tier(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Tier = apps.get_model('projects', 'Tier')
    for project in Project.objects.all():
        if project.governance is not None:
            governance, created = Tier.objects.get_or_create(type=project.governance)
            project.tier = governance
            project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220124_1053'),
    ]

    operations = [
        migrations.RunPython(link_tier),
    ]
