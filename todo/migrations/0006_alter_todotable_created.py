# Generated by Django 3.2.20 on 2023-10-13 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todotable_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotable',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 13, 14, 30, 36, 925608)),
        ),
    ]
