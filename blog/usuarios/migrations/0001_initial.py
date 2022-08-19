# Generated by Django 4.1 on 2022-08-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('contraseña', models.CharField(max_length=254)),
                ('usuarios', models.CharField(max_length=254)),
                ('tipoUsuario', models.CharField(choices=[('A', 'ADMIN'), ('V', 'VISITANTE')], default='V', max_length=1)),
            ],
        ),
    ]