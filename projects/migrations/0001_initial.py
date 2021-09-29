# Generated by Django 2.1.5 on 2021-09-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('Project', 'PROJECT'), ('Programme', 'PROGRAMME'), ('Portfolio', 'PORTFOLIO')], max_length=20)),
                ('abbreviation', models.CharField(max_length=20)),
                ('governance', models.CharField(blank=True, max_length=20, null=True)),
                ('stage', models.CharField(blank=True, max_length=20, null=True)),
                ('scope', models.TextField(blank=True, max_length=200, null=True)),
                ('live', models.BooleanField(default=True)),
            ],
        ),
    ]
