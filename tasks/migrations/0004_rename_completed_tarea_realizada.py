# Generated by Django 4.2.5 on 2023-09-12 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tarea_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='completed',
            new_name='realizada',
        ),
    ]