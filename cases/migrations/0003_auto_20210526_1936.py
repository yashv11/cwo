# Generated by Django 3.2.3 on 2021-05-26 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20210526_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportanonymously',
            name='Incident_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 19, 36, 52, 612158)),
        ),
        migrations.AlterField(
            model_name='reportanonymously',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 19, 36, 52, 611159)),
        ),
    ]
