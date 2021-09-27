# Generated by Django 2.1.5 on 2021-09-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('organisation', models.TextField()),
                ('group', models.TextField()),
                ('team', models.TextField()),
                ('role', models.TextField()),
                ('tele_no', models.TextField()),
                ('live', models.BooleanField(default=True)),
            ],
        ),
    ]
