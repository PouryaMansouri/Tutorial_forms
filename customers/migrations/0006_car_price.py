# Generated by Django 3.2.12 on 2022-02-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]