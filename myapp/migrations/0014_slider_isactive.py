# Generated by Django 5.0.4 on 2024-05-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='isactive',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
