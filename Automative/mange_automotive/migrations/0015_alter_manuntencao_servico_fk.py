# Generated by Django 4.2.3 on 2023-10-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0014_remove_manuntencao_servico_fk_manuntencao_servico_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuntencao',
            name='servico_fk',
            field=models.ManyToManyField(blank=True, default=None, to='mange_automotive.categoria_servico'),
        ),
    ]
