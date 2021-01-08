# Generated by Django 3.1.5 on 2021-01-08 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libro.categoria'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portada'),
        ),
    ]