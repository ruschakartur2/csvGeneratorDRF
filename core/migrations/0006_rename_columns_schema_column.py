# Generated by Django 3.2.6 on 2021-08-12 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210812_0634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='columns',
            new_name='column',
        ),
    ]