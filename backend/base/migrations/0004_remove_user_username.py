# Generated by Django 4.1 on 2022-12-20 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
