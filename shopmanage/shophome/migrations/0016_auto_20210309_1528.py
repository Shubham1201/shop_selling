# Generated by Django 3.1.7 on 2021-03-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shophome', '0015_auto_20210309_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='selling',
            field=models.FloatField(default=0),
        ),
    ]
