# Generated by Django 3.2.20 on 2023-10-13 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_table_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo_table',
            new_name='TodoTable',
        ),
    ]
