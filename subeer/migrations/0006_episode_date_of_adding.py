# Generated by Django 3.0.2 on 2020-06-17 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subeer', '0005_auto_20200616_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='date_of_adding',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of adding episode'),
        ),
    ]
