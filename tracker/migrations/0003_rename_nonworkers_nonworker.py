# Generated by Django 4.1.4 on 2022-12-20 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_nonworkers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='nonworkers',
            new_name='nonworker',
        ),
    ]
