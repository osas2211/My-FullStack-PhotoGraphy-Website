# Generated by Django 3.1.1 on 2020-12-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media/photos')),
            ],
        ),
        migrations.CreateModel(
            name='showcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=150)),
                ('showcase', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
