# Generated by Django 5.2.1 on 2025-06-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='Oylik'),
        ),
    ]
