# Generated by Django 4.0.4 on 2022-11-23 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subdepartment',
            name='department',
        ),
        migrations.AlterField(
            model_name='account',
            name='department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='SubDepartment',
        ),
    ]