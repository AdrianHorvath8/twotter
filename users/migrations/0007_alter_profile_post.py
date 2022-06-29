# Generated by Django 4.0.2 on 2022-06-29 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_tag'),
        ('users', '0006_profile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
