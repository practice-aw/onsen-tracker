# Generated by Django 3.0 on 2019-12-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20191218_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image_url',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='url',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='yelp_id',
            field=models.CharField(max_length=140),
        ),
    ]
