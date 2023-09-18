# Generated by Django 4.2.1 on 2023-09-18 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_date_joined_user_datetime_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]