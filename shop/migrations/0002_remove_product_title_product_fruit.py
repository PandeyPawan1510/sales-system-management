# Generated by Django 4.2.6 on 2023-11-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='fruit',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
