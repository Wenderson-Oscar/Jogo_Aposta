from django.test import TestCase
from random import sample
# Create your tests here.

def logica_loteria():
    """Lógica da loteria"""
    sorteio = sample(range(1, 61), 6)
    bilhete = ['23','34','3','22','40','50']

    print(sorteio, bilhete)
    print(set(map(str,sorteio)) & set(bilhete))


def combinacao_bicho():
    """Lógica do bicho"""
    bicho = sample(range(1,100), 4)
    escolha  = ['1','2','3','4','9','10','11','12']
    comb = set(map(str, bicho)) & set(escolha)
    print('N° bicho',bicho,'\nescolha',escolha, '\ncombinação',comb)


def premiu_bichos():
    """Lógica do bicho"""
    sort = sample(range(0, 100), 2)
    sort.reverse()
    escolha  = [1,2,3,4,9,10,11,12]
    resultado = set(sort) & set(escolha)
    print(f'Sorteado: {sort}\nEscolhido: {escolha}\nResultado: {resultado}')


premiu_bichos()