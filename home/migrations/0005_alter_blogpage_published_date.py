# Generated by Django 5.0 on 2023-12-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blogpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]