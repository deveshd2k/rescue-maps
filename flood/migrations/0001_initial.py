# Generated by Django 2.1.2 on 2018-10-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='floodTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.IntegerField(blank=True, default=0)),
                ('rescueHome', models.CharField(max_length=30)),
                ('orgName', models.CharField(max_length=50)),
                ('orgAddress', models.CharField(max_length=50)),
                ('orgNumber', models.CharField(max_length=12)),
                ('bedsNo', models.IntegerField(blank=True, default=0)),
                ('transport', models.CharField(max_length=5)),
                ('bloodBank', models.CharField(max_length=5)),
                ('sBags', models.CharField(max_length=5)),
                ('blankets', models.CharField(max_length=5)),
            ],
        ),
    ]