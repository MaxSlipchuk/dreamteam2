# Generated by Django 4.2.5 on 2023-12-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_page', '0003_alter_perfum_description_alter_perfum_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfum',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Зображення'),
        ),
    ]