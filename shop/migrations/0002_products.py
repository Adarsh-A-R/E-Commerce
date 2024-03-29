# Generated by Django 5.0.1 on 2024-02-18 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('img', models.ImageField(upload_to='product')),
                ('des', models.TextField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categ')),
            ],
        ),
    ]
