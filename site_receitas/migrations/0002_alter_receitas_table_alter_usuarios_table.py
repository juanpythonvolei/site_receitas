# Generated by Django 5.1.6 on 2025-02-10 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='receitas',
            table='Receitas',
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='Usuarios',
        ),
    ]
