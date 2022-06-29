# Generated by Django 4.0.2 on 2022-06-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag', to='posts.Tag'),
        ),
    ]
