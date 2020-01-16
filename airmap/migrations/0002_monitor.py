# Generated by Django 2.2.7 on 2020-01-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_reading', models.CharField(max_length=30)),
                ('latest_reading_datetime', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
