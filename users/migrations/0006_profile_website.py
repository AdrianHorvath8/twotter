# Generated by Django 4.0.5 on 2022-06-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]