# Generated by Django 3.1.4 on 2020-12-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0008_auto_20201226_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
