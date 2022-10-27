from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)


    def __str__(self):
        return self.nome


class Carteira(models.Model):

    carteira = models.FloatField(default=10)
    cliente = models.OneToOneField(User, on_delete=models.CASCADE, null=False)


    """JOGOS"""

class MegaSena(models.Model):

    data = models.DateField()
    sorteio = models.JSONField()

    def __str__(self):
        return f'{self.sorteio}'


class JogoBicho(models.Model):

    BICHOS = (
        ("1,2,3,4", "Avestruz"),
        ("5,6,7,8", "Àguia"),
        ("9,10,11,12", "Burro"),
        ("13,14,15,16", "Borboleta"),
        ("17,18,19,20", "Cachorro"),
        ("21,22,23,24", "Cabra"),
        ("25,26,27,28", "Carneiro"),
        ("29,30,31,32", "Camelo"),
        ("33,34,35,36", "Cobra"),
        ("37,38,39,40", "Coelho"),
        ("41,42,43,44", "Cavalo"),
        ("45,46,47,48", "Elefante"),
        ("49,50,51,52", "Galo"),
        ("53,54,55,56", "Gato"),
        ("57,58,59,60", "Jacaré"),
        ("61,62,63,64", "Leão"),
        ("65,66,67,68", "Macaco"),
        ("69,70,71,72", "Porco"),
        ("73,74,75,76", "Pavão"),
        ("77,78,79,80", "Perú"),
        ("81,82,83,84", "Touro"),
        ("85,86,87,88", "Tigre"),
        ("89,90,91,92", "Urso"),
        ("93,94,95,96", "Veado"),
        ("97,98,99,00", "Vaca"),
    )


    data = models.DateField()
    bichos = models.JSONField(choices = BICHOS)
    ligacao = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.bichos}'