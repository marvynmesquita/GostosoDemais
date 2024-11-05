# Generated by Django 5.1.2 on 2024-11-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_remove_ingredientes_quantidade_receitas_quantidade"),
    ]

    operations = [
        migrations.CreateModel(
            name="quantidade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="receitas",
            name="ingredientes",
        ),
        migrations.RemoveField(
            model_name="receitas",
            name="quantidade",
        ),
    ]
