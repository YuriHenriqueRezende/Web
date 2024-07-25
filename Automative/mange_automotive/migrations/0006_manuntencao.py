# Generated by Django 4.2.3 on 2023-10-04 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0005_categoria_automovel'),
    ]

    operations = [
        migrations.CreateModel(
            name='manuntencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automovel_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_automovel', to='mange_automotive.categoria_automovel')),
                ('funcionario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='mange_automotive.funcionario')),
                ('logistica_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logistica_loja', to='mange_automotive.logistica_loja')),
                ('servico_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_servico', to='mange_automotive.categoria_servico')),
            ],
        ),
    ]
