# Generated by Django 2.1.5 on 2021-10-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagements', '0015_engagementtype_engagementworkstream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engagement',
            name='type',
        ),
        migrations.RemoveField(
            model_name='engagement',
            name='ws_type',
        ),
        migrations.AddField(
            model_name='engagement',
            name='engagement_types',
            field=models.ManyToManyField(to='engagements.EngagementType'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='engagement_workstreams',
            field=models.ManyToManyField(to='engagements.EngagementWorkStream'),
        ),
    ]
