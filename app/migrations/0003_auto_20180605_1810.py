# Generated by Django 2.0.5 on 2018-06-05 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 6, 5, 16, 10, 28, 547731, tzinfo=utc)),
        ),
    ]