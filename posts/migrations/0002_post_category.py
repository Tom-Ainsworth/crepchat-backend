# Generated by Django 4.1.1 on 2022-09-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("ADIDAS", "Adidas"),
                    ("NEW_BALANCE", "New Balance"),
                    ("NIKE", "Nike"),
                ],
                default="Nike",
                max_length=20,
            ),
        ),
    ]
