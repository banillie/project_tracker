# Generated by Django 2.1.5 on 2021-09-30 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engagements', '0008_auto_20210930_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engagement',
            name='ppdd',
        ),
        migrations.RemoveField(
            model_name='engagement',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='engagement',
            name='stakeholder',
        ),
        migrations.RemoveField(
            model_name='engagementprojects',
            name='engagement',
        ),
        migrations.RemoveField(
            model_name='engagementprojects',
            name='project',
        ),
        migrations.DeleteModel(
            name='Engagement',
        ),
        migrations.DeleteModel(
            name='EngagementProjects',
        ),
    ]