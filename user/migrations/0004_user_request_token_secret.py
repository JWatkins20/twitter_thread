# Generated by Django 3.0.6 on 2020-05-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='request_token_secret',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]