# Generated by Django 4.0 on 2022-01-01 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0006_rename_active_category_cat_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='cat_update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]