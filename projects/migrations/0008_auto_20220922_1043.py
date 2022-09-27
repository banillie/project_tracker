# Generated by Django 3.2 on 2022-09-22 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20220922_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='sort',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.type', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sort',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.type', verbose_name='Type'),
        ),
    ]