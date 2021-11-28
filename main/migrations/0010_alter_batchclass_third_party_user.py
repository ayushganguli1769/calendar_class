# Generated by Django 3.2.9 on 2021-11-24 16:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_alter_task_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchclass',
            name='third_party_user',
            field=models.ManyToManyField(related_name='anonymous_classes', to=settings.AUTH_USER_MODEL),
        ),
    ]
