# Generated by Django 4.1 on 2023-01-01 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_remove_products_user_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='user',
        ),
    ]
