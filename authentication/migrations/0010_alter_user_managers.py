# Generated by Django 4.2.1 on 2023-09-18 23:43

import authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_user_username_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
    ]
