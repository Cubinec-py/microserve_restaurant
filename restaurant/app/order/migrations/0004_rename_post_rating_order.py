# Generated by Django 4.1.5 on 2023-02-05 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='post',
            new_name='order',
        ),
    ]
