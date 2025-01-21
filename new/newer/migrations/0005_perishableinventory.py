# Generated by Django 5.0.6 on 2025-01-20 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newer', '0004_alter_inventory_category_alter_inventory_item_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerishableInventory',
            fields=[
                ('inventory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='newer.inventory')),
                ('expiration_date', models.DateField()),
            ],
            bases=('newer.inventory',),
        ),
    ]