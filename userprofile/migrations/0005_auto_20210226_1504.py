# Generated by Django 3.1.2 on 2021-02-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20210222_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='userA',
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics/{user.username}'),
        ),
    ]
