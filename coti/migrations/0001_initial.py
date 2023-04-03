# Generated by Django 4.1.7 on 2023-04-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=30)),
                ('numero', models.IntegerField(verbose_name=30)),
                ('dni', models.IntegerField(verbose_name=30)),
                ('cp', models.IntegerField(verbose_name=30)),
                ('mensaje', models.TextField(blank=True)),
            ],
        ),
    ]