# Generated by Django 2.2.6 on 2019-10-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0002_auto_20191007_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
