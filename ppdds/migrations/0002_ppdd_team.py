# Generated by Django 2.1.5 on 2021-09-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppdds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppdd',
            name='team',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
