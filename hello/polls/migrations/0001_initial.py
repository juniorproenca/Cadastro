# Generated by Django 2.2 on 2019-06-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino'], ['N', 'Nenhuma das opções']], max_length=1)),
                ('grau', models.CharField(choices=[['EM', 'Ensino Medio'], ['ES', 'Ensino Superior'], ['N', 'Nenhuma das opções']], max_length=1)),
                ('naturalidade', models.CharField(choices=[['EM', 'Brasil'], ['ES', 'Espanha'], ['N', 'Nenhuma das opções']], max_length=1)),
            ],
        ),
    ]