# Generated by Django 4.1 on 2022-08-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.CharField(max_length=254),
        ),
    ]