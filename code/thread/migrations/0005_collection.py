# Generated by Django 3.1.4 on 2020-12-26 21:20

from django.conf import settings
from django.db import migrations, models
import thread.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thread', '0004_auto_20201225_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=400)),
                ('status', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=200)),
                ('added_by', models.ForeignKey(on_delete=models.SET(thread.models.get_deleted_user), to=settings.AUTH_USER_MODEL)),
                ('threads', models.ManyToManyField(to='thread.Thread')),
            ],
        ),
    ]