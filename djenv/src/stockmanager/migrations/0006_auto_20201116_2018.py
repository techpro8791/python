# Generated by Django 3.1.3 on 2020-11-16 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanager', '0005_auto_20201116_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_CSV',
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stockmanager.category'),
        ),
    ]