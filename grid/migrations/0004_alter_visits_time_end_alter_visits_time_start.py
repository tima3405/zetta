# Generated by Django 4.0.2 on 2022-02-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0003_alter_visits_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='time_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visits',
            name='time_start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
