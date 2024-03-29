# Generated by Django 4.0.2 on 2022-07-18 10:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_message_is_read'),
        ('posts', '0015_topic_remove_post_tag_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
