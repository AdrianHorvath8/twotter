# Generated by Django 4.0.2 on 2022-06-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
