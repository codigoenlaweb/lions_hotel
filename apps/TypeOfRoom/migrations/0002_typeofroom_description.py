# Generated by Django 4.0.4 on 2022-05-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypeOfRoom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofroom',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
