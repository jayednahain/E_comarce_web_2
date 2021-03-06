# Generated by Django 4.0 on 2022-01-10 11:51

import Utilities.media_path_convertor
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('product_description', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to=Utilities.media_path_convertor.upload_product_image_path)),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_app.category')),
            ],
        ),
    ]
