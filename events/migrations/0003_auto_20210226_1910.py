# Generated by Django 3.1.5 on 2021-02-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210219_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]