# Generated by Django 3.2 on 2021-11-04 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engagements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engagement',
            name='user',
        ),
    ]
