# Generated by Django 4.0.2 on 2022-07-18 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_message_is_read'),
        ('posts', '0018_alter_bookmark_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='post',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
