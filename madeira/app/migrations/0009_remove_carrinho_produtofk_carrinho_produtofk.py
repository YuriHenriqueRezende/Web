# Generated by Django 5.0.6 on 2024-05-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_produto_subprodutofk_delete_sub_produto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='produtoFK',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produtoFK',
            field=models.ManyToManyField(to='app.produto'),
        ),
    ]
