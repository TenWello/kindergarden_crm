# Generated by Django 5.2.1 on 2025-05-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='min_quantity',
        ),
    ]
