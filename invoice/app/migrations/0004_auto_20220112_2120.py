# Generated by Django 3.2.3 on 2022-01-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_producat_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='address',
            field=models.CharField(default='IFCO Chowk, Delhi', max_length=150),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(default='Vikas Sharma', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(default='+91 8171415434'),
        ),
    ]
