# Generated by Django 3.2 on 2022-02-24 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Project', 'PROJECT'), ('Programme', 'PROGRAMME'), ('Portfolio', 'PORTFOLIO')], max_length=20)),
                ('abbreviation', models.CharField(max_length=20)),
                ('governance', models.CharField(blank=True, max_length=20, null=True)),
                ('stage', models.CharField(blank=True, max_length=20, null=True)),
                ('scope', models.TextField(blank=True, max_length=200, null=True)),
                ('live', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.tier')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Project', 'PROJECT'), ('Programme', 'PROGRAMME'), ('Portfolio', 'PORTFOLIO')], max_length=20)),
                ('abbreviation', models.CharField(max_length=20)),
                ('governance', models.CharField(blank=True, max_length=20, null=True)),
                ('stage', models.CharField(blank=True, max_length=20, null=True)),
                ('scope', models.TextField(blank=True, max_length=200, null=True)),
                ('live', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tier', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.tier')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical project',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
