# Generated by Django 4.1.5 on 2023-01-30 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_order_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='waiter',
        ),
    ]
