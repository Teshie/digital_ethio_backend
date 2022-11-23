# Generated by Django 4.0.4 on 2022-11-23 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdepartment',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='department.department')),
            ],
        ),
    ]