# Generated by Django 3.2.7 on 2021-12-05 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0006_alter_pharmacy_user'),
        ('Admin_pharmacy', '0007_purchase_pharmacys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='pharmacy.pharmacy'),
        ),
    ]
