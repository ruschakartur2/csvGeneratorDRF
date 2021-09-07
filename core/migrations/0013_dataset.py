# Generated by Django 3.2.6 on 2021-09-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210902_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('rows', models.IntegerField()),
                ('modification', models.DateTimeField(auto_now=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schema', to='core.schema')),
            ],
        ),
    ]