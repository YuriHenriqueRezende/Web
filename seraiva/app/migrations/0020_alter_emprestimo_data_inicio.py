# Generated by Django 5.0.6 on 2024-05-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_emprestimo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_inicio',
            field=models.DateField(auto_now_add=True),
        ),
    ]
