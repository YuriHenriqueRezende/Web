# Generated by Django 4.2.3 on 2023-10-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0013_alter_categoria_servico_valor_obra_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manuntencao',
            name='servico_fk',
        ),
        migrations.AddField(
            model_name='manuntencao',
            name='servico_fk',
            field=models.ManyToManyField(to='mange_automotive.categoria_servico'),
        ),
    ]
