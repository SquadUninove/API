# Generated by Django 3.2.7 on 2021-09-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]