from django.db import models

# Create your models here.
class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]
    grau_de_instrucao = [
        ["EM", "Ensino Medio"],
        ["ES", "Ensino Superior"],
        ["N", "Nenhuma das opções"]
    ]

    naturalidade2 = [
        ["EM", "Brasil"],
        ["ES", "Espanha"],
        ["N", "Nenhuma das opções"]
    ]




    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES)
    grau = models.CharField(max_length=15, choices=grau_de_instrucao)
    naturalidade = models.CharField(max_length=15, choices=naturalidade2)



 