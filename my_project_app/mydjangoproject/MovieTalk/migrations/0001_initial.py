# Generated by Django 4.2.16 on 2024-10-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=9000)),
                ('duration', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
