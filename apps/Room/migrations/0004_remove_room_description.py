# Generated by Django 4.0.4 on 2022-05-01 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0003_alter_room_type_of_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
    ]
