# Generated by Django 3.1.5 on 2021-01-10 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_libro_categoria'),
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro'),
        ),
    ]
