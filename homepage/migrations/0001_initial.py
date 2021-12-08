# Generated by Django 3.2.7 on 2021-12-02 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter_subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suscriber_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='dr_blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3000)),
                ('desc', models.TextField(max_length=10000)),
                ('date', models.DateField()),
                ('img', models.ImageField(null=True, upload_to='')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dr_bilogs', to='doctors.dr')),
            ],
        ),
    ]
