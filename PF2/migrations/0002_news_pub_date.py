# Generated by Django 3.1 on 2020-08-18 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PF2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 18, 14, 42, 36, 943224, tzinfo=utc)),
        ),
    ]
