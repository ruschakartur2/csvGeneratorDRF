# Generated by Django 3.2.6 on 2021-08-11 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210811_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='column',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.schemacolumn'),
            preserve_default=False,
        ),
    ]
