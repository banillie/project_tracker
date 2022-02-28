# Generated by Django 3.2 on 2022-02-28 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0005_remove_dftgroup_organisation'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='dft_group',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='stakeholders.dftgroup'),
        ),
        migrations.AddField(
            model_name='project',
            name='dft_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stakeholders.dftgroup'),
        ),
    ]
