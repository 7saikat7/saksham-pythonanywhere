# Generated by Django 3.1.1 on 2020-09-19 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='gallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=30)),
                ('url', models.URLField(blank=True)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='Media')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicat_name', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('contact_number', models.DecimalField(decimal_places=0, max_digits=15, null=True)),
                ('upload', models.ImageField(null=True, upload_to='usermedia')),
                ('user', models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
