# Generated by Django 2.2.4 on 2019-10-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='return_date',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
