# Generated by Django 4.2.5 on 2023-12-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
