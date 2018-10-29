# Generated by Django 2.1.2 on 2018-10-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0006_remove_floodtable_orgnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='rescueTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rescueHome', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('lattitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Coordinates',
        ),
    ]
