# Generated by Django 4.0.6 on 2022-08-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_glasses_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]
