# Generated by Django 5.0.4 on 2024-05-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_checkout_address1_remove_checkout_address2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalamt', models.CharField(max_length=255)),
                ('payment_mode', models.CharField(max_length=100)),
                ('order_status', models.CharField(max_length=100)),
                ('order_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
