# Generated by Django 4.0.4 on 2022-05-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0007_alter_reservation_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=5, verbose_name='Confirmation_code'),
        ),
    ]
