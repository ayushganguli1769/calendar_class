# Generated by Django 3.2.9 on 2021-11-15 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0002_alter_extendeduser_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_code_student', models.CharField(max_length=200)),
                ('batch_code_teacher', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=500)),
                ('all_users_in_batch', models.ManyToManyField(related_name='all_batch_user_belongs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BatchClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('belongs_to_batch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='all_batch_class', to='main.batch')),
                ('teachers', models.ManyToManyField(related_name='classes_teaching', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('stress_level', models.IntegerField(default=5)),
                ('description', models.CharField(max_length=15500)),
                ('belongs_to_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='batch_class_tasks', to='main.batchclass')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_submission', models.DateTimeField(auto_now_add=True)),
                ('belongs_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_task_submission', to=settings.AUTH_USER_MODEL)),
                ('for_which_task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_submissions', to='main.task')),
            ],
        ),
        migrations.CreateModel(
            name='FileStored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('stored_file', models.FileField(null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
