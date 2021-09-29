# Generated by Django 2.1.5 on 2021-09-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0007_delete_stakeholder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('summary', models.TextField()),
                ('follow_up_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEngagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engagement', models.ManyToManyField(to='engagements.Engagement')),
                ('project', models.ManyToManyField(to='projects.Project')),
            ],
        ),
    ]
