# Generated by Django 2.1.2 on 2018-10-13 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0005_remove_floodtable_rescuehome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floodtable',
            name='orgNumber',
        ),
    ]
