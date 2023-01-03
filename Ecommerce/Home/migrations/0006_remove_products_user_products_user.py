# Generated by Django 4.1 on 2023-01-01 09:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0005_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='user',
        ),
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]