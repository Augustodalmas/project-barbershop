# Generated by Django 5.0.4 on 2024-10-12 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barbeiro',
            name='contrato',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cpf',
        ),
        migrations.AddField(
            model_name='barbeiro',
            name='barbershop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.barbershop'),
        ),
        migrations.AddField(
            model_name='barbeiro',
            name='cpf',
            field=models.CharField(blank=True, default='000.000.000-00', max_length=14),
        ),
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')], default='Outros', max_length=10),
        ),
        migrations.AlterField(
            model_name='proprietário',
            name='propriedade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.barbershop'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero_telefone',
            field=models.CharField(blank=True, default='(00)00000-0000', max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
