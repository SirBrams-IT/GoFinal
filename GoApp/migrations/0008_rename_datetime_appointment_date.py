# Generated by Django 5.1.2 on 2024-11-18 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GoApp', '0007_delete_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='datetime',
            new_name='date',
        ),
    ]
