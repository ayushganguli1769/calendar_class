# Generated by Django 3.2.9 on 2021-11-22 19:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_batchclass_student_class_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestored',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 22, 19, 52, 30, 397643, tzinfo=utc)),
            preserve_default=False,
        ),
    ]