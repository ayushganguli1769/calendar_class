# Generated by Django 3.2.9 on 2021-11-14 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(null=True)),
                ('is_student', models.BooleanField(default=True)),
                ('linked_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended_reverse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
