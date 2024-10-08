# Generated by Django 5.1 on 2024-09-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.CharField(default='I love fruits'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='apple.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=150.99, max_digits=10),
        ),
    ]
