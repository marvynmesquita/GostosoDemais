# Generated by Django 5.1.2 on 2024-10-30 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categorias",
            name="descricao",
        ),
    ]
