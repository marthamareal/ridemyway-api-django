# Generated by Django 2.1.7 on 2019-09-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.CharField(choices=[('CR', 'Car'), ('BK', 'Bike')], default='CR', max_length=5),
        ),
    ]