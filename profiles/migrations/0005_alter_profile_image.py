# Generated by Django 3.2 on 2023-04-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default_profile_kkzjl7_tv9li6.jpg', upload_to='images/'),
        ),
    ]
