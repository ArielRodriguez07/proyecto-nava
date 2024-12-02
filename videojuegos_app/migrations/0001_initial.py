# Generated by Django 5.1.2 on 2024-11-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('id_videojuego', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('plataforma', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('fecha_lanzamiento', models.DateField()),
            ],
        ),
    ]