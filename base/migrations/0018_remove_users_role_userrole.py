# Generated by Django 4.0.6 on 2022-08-17 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_users_organisation_users_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='role',
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Develpoer', 'Developer'), ('Tester', 'Tester'), ('QA', 'QA'), ('Manager', 'Manager'), ('Team Lead', 'Team Lead')], default='Developer', max_length=50, null=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organisation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
            options={
                'verbose_name': 'UserRole',
            },
        ),
    ]