# Generated by Django 4.0.2 on 2022-02-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='reason',
            field=models.CharField(blank=True, default=' ', max_length=1000, null=True),
        ),
    ]
