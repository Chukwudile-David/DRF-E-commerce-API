# Generated by Django 4.0.1 on 2022-08-22 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('EcommerceApp', '0004_book_created_by_product_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(to='EcommerceApp.Book')),
                ('products', models.ManyToManyField(to='EcommerceApp.Product')),
            ],
            options={
                'ordering': ['cart_id', 'created_at'],
            },
        ),
    ]
