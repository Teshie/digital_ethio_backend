# Generated by Django 4.0.4 on 2022-11-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
