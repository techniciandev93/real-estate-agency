# Generated by Django 3.2.21 on 2023-09-30 12:27

from django.db import migrations


def flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()

    for flat_obj in flats:
       Owner.objects.get_or_create(owner=flat_obj.owner,
                                   owners_phonenumber=flat_obj.owners_phonenumber,
                                   owner_pure_phone=flat_obj.owners_phonenumber,
                                   )


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.RunPython(flats_to_owners, move_backward)
    ]