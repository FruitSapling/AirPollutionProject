# Generated by Django 2.2.7 on 2020-01-07 10:48

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('airmap', '0002_monitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='geom',
            field=djgeojson.fields.PointField(default={'coordinates': [-1.4058208465576172, 47.15301133231325], 'type': 'Point'}),
        ),
    ]