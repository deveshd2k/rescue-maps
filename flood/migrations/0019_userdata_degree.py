# Generated by Django 2.1.2 on 2018-10-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0018_remove_userdata_rescuelevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='degree',
            field=models.FloatField(default=0),
        ),
    ]
