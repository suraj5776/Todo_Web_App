# Generated by Django 3.2.20 on 2023-10-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_todo_table_todotable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotable',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
