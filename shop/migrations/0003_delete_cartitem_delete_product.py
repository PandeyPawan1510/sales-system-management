# Generated by Django 4.2.1 on 2024-04-08 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_title_product_fruit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
