# Generated by Django 2.2.6 on 2019-10-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0014_auto_20191011_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(null=True),
        ),
    ]