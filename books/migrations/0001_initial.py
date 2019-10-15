# Generated by Django 2.2.4 on 2019-09-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(default='', max_length=10)),
                ('title', models.CharField(default='', max_length=30)),
                ('author', models.CharField(default='', max_length=30)),
                ('publisher', models.CharField(default='', max_length=30)),
                ('rack_no', models.CharField(default='', max_length=5)),
                ('no_of_copies', models.IntegerField()),
            ],
        ),
    ]