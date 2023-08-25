# Generated by Django 4.2.1 on 2023-08-25 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_rename_date_joined_user_datetime_joined_and_more'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('value', models.FloatField()),
                ('status', models.IntegerField(choices=[(1, 'Remove - transaction'), (2, 'Remove - expiration date'), (3, 'Remove - manual'), (4, 'Add'), (5, 'Devolution')])),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('quantity', models.IntegerField()),
                ('barcode', models.CharField(max_length=32)),
                ('base_price', models.FloatField()),
                ('commercial_price', models.FloatField()),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Teste',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.tag'),
        ),
        migrations.AddField(
            model_name='historic',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='historic',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.transaction'),
        ),
    ]
