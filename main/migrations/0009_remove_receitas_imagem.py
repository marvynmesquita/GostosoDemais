# Generated by Django 5.1.2 on 2024-11-05 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_remove_receitas_criador"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="receitas",
            name="imagem",
        ),
    ]