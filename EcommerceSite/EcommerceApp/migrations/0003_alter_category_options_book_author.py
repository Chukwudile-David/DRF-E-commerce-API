# Generated by Django 4.0.1 on 2022-08-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0002_remove_product_description_remove_product_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='John Doe', max_length=100),
        ),
    ]
