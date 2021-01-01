# Generated by Django 3.1.4 on 2021-01-01 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thread', '0016_remove_thread_length_owned'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ('brand', 'id_number')},
        ),
        migrations.CreateModel(
            name='OwnedThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_owned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('owned_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread.thread')),
            ],
            options={
                'ordering': ('owned_thread',),
            },
        ),
    ]
