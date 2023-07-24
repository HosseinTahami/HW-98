# Generated by Django 4.2.3 on 2023-07-21 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0015_alter_task_due_date_alter_task_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 22, 9, 2, 25, 255876)),
        ),
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(default='/images/task_default.png', upload_to='images/'),
        ),
    ]