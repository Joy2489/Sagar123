# Generated by Django 5.0.4 on 2024-04-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_enquiry_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='DOB',
            field=models.DateField(default='0000-00-00'),
        ),
    ]
