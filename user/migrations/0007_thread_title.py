# Generated by Django 3.0.8 on 2020-07-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_post_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.TextField(default='title'),
        ),
    ]
