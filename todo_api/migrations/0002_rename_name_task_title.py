# Generated by Django 4.0 on 2022-01-02 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Name',
            new_name='Title',
        ),
    ]
