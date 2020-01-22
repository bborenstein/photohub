# Generated by Django 3.0.2 on 2020-01-21 18:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photographers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('blogcopy_main', models.TextField(blank=True)),
                ('blogcopy_1', models.TextField(blank=True)),
                ('blogcopy_2', models.TextField(blank=True)),
                ('blogcopy_3', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_10', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_11', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_12', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('posted_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='photographers.Photographer')),
            ],
        ),
    ]