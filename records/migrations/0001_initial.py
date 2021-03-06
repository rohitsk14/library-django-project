# Generated by Django 2.2.4 on 2019-10-01 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(default='', max_length=10)),
                ('student_id', models.CharField(default='', max_length=15)),
                ('student_name', models.CharField(default='', max_length=30)),
                ('year', models.CharField(default='', max_length=10)),
                ('issue_date', models.DateTimeField(default=datetime.datetime.now)),
                ('return_date', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
