# Generated by Django 2.2.12 on 2022-04-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='rollno',
            field=models.IntegerField(),
        ),
    ]