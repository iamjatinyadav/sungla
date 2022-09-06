# Generated by Django 4.0.6 on 2022-08-17 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_organisation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='organisation',
        ),
        migrations.AddField(
            model_name='users',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.organisation'),
        ),
    ]
