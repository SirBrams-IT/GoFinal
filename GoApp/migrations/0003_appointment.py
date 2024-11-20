# Generated by Django 5.1.2 on 2024-11-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoApp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('datetime', models.DateTimeField()),
                ('department', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=60)),
                ('message', models.TextField()),
            ],
        ),
    ]
