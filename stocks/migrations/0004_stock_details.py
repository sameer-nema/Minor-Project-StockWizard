# Generated by Django 3.1.7 on 2021-05-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('uname', models.CharField(max_length=100)),
            ],
        ),
    ]