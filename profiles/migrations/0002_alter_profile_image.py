# Generated by Django 3.2 on 2023-04-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_xwccjc.jpg', upload_to='images/'),
        ),
    ]