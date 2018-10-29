# Generated by Django 2.1.2 on 2018-10-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0013_auto_20181026_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=13)),
                ('family', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rescuelevel',
            field=models.CharField(default='10', max_length=10),
        ),
    ]