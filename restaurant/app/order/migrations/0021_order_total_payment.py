# Generated by Django 4.1.5 on 2023-02-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_remove_orderitem_tips_order_tips'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_payment',
            field=models.IntegerField(default=0),
        ),
    ]