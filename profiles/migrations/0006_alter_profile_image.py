# Generated by Django 3.2 on 2023-04-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_kkzjl7.jpg', upload_to='images/'),
        ),
    ]