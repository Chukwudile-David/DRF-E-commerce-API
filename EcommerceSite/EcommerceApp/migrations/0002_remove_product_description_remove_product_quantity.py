# Generated by Django 4.1 on 2022-08-16 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
