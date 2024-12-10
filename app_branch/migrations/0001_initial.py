# Generated by Django 5.1.3 on 2024-12-09 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branches', to=settings.AUTH_USER_MODEL, verbose_name='Manager')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='app_company.restaurantmodel', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
