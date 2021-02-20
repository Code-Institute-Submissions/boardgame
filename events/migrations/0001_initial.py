# Generated by Django 3.1.5 on 2021-02-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('offsite_url', models.URLField(blank=True)),
                ('member_only', models.BooleanField()),
                ('signed_up_users', models.ManyToManyField(to='profiles.UserProfile')),
            ],
        ),
    ]