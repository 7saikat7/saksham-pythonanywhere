# Generated by Django 3.1.1 on 2020-09-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200919_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
        migrations.AlterField(
            model_name='upload',
            name='applicat_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
