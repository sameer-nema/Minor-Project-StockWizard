# Generated by Django 3.1.7 on 2021-05-26 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_stock_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock_details',
            new_name='Stock_detail',
        ),
    ]
