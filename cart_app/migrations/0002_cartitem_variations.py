# Generated by Django 4.0 on 2022-01-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variation_app', '0001_initial'),
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='variation_app.Variation'),
        ),
    ]