# Generated by Django 4.2.5 on 2024-02-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_page', '0006_perfum_count_in_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfum',
            name='count_in_cart',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]