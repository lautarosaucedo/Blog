# Generated by Django 4.1 on 2022-08-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]