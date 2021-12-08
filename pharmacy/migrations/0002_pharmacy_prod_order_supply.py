# Generated by Django 3.2.7 on 2021-12-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_pharmacy', '0001_initial'),
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy_prod_order',
            name='supply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supp', to='Admin_pharmacy.supplier'),
        ),
    ]