# Generated by Django 4.1 on 2022-08-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvmodel',
            name='Year_Of_Publication',
            field=models.BigIntegerField(null=True),
        ),
    ]
