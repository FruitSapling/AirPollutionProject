# Generated by Django 2.2.7 on 2020-01-07 10:51

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('airmap', '0003_monitor_geom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='geom',
        ),
        migrations.AddField(
            model_name='monitor',
            name='poo',
            field=djgeojson.fields.PointField(default={'coordinates': [-1.4058208465576172, 47.15301133231325], 'type': 'Point'}),
        ),
    ]
