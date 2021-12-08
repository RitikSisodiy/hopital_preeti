# Generated by Django 3.2.7 on 2021-12-04 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20211202_2037'),
        ('pharmacy', '0003_pha_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='user',
            field=models.OneToOneField(default='ppp', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_register_record', to='doctors.usertype'),
        ),
    ]