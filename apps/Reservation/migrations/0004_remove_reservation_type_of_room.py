# Generated by Django 4.0.4 on 2022-04-28 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0003_reservation_type_of_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='type_of_room',
        ),
    ]
