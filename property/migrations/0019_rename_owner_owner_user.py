# Generated by Django 3.2.21 on 2023-10-07 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20231006_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='user',
        ),
    ]