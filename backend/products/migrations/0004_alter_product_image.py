# Generated by Django 5.1 on 2024-09-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='apple.jpg', upload_to=''),
        ),
    ]
