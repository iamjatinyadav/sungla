# Generated by Django 4.0.6 on 2022-08-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_users_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='role',
        ),
        migrations.AddField(
            model_name='organisation',
            name='role',
            field=models.CharField(blank=True, choices=[('Developer', 'Developer'), ('Tester', 'Tester'), ('QA', 'QA'), ('Manager', 'Manager'), ('Team Lead', 'Team Lead')], default='Developer', max_length=50, null=True),
        ),
    ]
