# Generated by Django 4.1 on 2022-08-17 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('detalles', models.CharField(max_length=255)),
                ('fecha', models.TimeField()),
                ('images', models.ImageField(upload_to='images_post')),
                ('categorias', models.ManyToManyField(related_name='categorias', to='post.categoria')),
                ('idUsuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
    ]