# Generated by Django 3.1.4 on 2020-12-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0009_auto_20201226_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
