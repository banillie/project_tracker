# Generated by Django 2.1.5 on 2021-09-29 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engagements', '0002_auto_20210929_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement',
            name='project',
            field=models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, to='projects.Project', to_field='name'),
        ),
    ]
