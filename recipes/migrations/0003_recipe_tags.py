# Generated by Django 5.0.3 on 2024-04-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_recipe_title"),
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(to="tags.tag"),
        ),
    ]
