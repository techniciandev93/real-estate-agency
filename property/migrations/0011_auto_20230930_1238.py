# Generated by Django 3.2.21 on 2023-09-30 09:38

from django.db import migrations
from django.core.paginator import Paginator
import phonenumbers


def recording_phone_numbers(objects, model):
    flats = []
    for obj in objects:
        phone_number = phonenumbers.parse(obj.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(phone_number):
            e164_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
            obj.owner_pure_phone = e164_format
            flats.append(obj)
    model.objects.bulk_update(flats, ['owner_pure_phone'])


def change_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    flat_objects = Flat.objects.all()
    paginator = Paginator(flat_objects, 500)
    for page in paginator.page_range:
        current_page = paginator.page(page)
        recording_phone_numbers(current_page.object_list, Flat)


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone='')


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_alter_flat_like'),
    ]

    operations = [
        migrations.RunPython(change_owner_pure_phone, move_backward)
    ]
