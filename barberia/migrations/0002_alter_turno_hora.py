# Generated by Django 5.0.dev20230808072628 on 2023-11-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barberia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='hora',
            field=models.TimeField(max_length=50),
        ),
    ]
