# Generated by Django 2.2.24 on 2023-09-29 11:59

from django.db import migrations

YEAR = 2015


def change_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=YEAR).update(new_building=True)
    Flat.objects.filter(construction_year__lt=YEAR).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230929_1414'),
    ]

    operations = [
        migrations.RunPython(change_new_building),
    ]
