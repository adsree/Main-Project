# Generated by Django 4.2.3 on 2023-12-04 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_cart_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blogs',
            table='Blogs',
        ),
        migrations.AlterModelTable(
            name='reviews',
            table='Reviews',
        ),
    ]
