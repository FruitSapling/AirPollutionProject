# Generated by Django 2.2.7 on 2020-01-16 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('airmap', '0008_auto_20200116_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 16, 13, 27, 44, 869315, tzinfo=utc)),
        ),
    ]
