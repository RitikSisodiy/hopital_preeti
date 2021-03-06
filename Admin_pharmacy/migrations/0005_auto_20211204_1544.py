# Generated by Django 3.2.7 on 2021-12-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_pharmacy', '0004_alter_pharmacy_admin_record_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
