# Generated by Django 3.1.2 on 2021-02-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20210226_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
