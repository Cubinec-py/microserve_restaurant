# Generated by Django 4.1.5 on 2023-02-06 23:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryDish",
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
                ("name", models.CharField(max_length=200)),
                ("image", models.ImageField(null=True, upload_to="category_dishes")),
            ],
        ),
        migrations.CreateModel(
            name="Dish",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("description", models.TextField(max_length=1000)),
                ("amount", models.IntegerField(default=0)),
                ("weight", models.IntegerField(default=0)),
                ("image", models.ImageField(null=True, upload_to="dishes")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Не доступно", "Не доступно"),
                            ("Доступно", "Доступно"),
                        ],
                        default="Доступно",
                        max_length=100,
                    ),
                ),
                ("category", models.ManyToManyField(to="products.categorydish")),
            ],
        ),
    ]