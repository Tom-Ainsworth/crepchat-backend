# Generated by Django 4.1.1 on 2022-09-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="title",
            new_name="caption",
        ),
        migrations.RemoveField(
            model_name="post",
            name="content",
        ),
    ]
