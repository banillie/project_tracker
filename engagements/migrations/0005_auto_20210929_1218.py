# Generated by Django 2.1.5 on 2021-09-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engagements', '0004_auto_20210929_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
