# Generated by Django 3.2.9 on 2021-11-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
