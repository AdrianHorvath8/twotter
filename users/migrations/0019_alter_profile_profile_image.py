# Generated by Django 4.0.2 on 2022-07-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profiles/user-default.png', upload_to='profiles/'),
        ),
    ]
