# Generated by Django 4.0.4 on 2022-04-27 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TypeOfRoom', '0001_initial'),
        ('Reservation', '0002_remove_reservation_type_of_room_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='type_of_room',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='TypeOfRoom.typeofroom', verbose_name='Type of room'),
            preserve_default=False,
        ),
    ]
