# Generated by Django 5.0 on 2024-03-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Shades', 'Shades'), ('For_men', 'For_men'), ('For_women', 'For_women'), ('For_kids', 'For_kids'), ('Watches', 'Watches')], max_length=150),
        ),
    ]
