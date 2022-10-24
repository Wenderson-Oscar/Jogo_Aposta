from django.test import TestCase
from random import sample
# Create your tests here.

"""Lógica da loteria"""

sorteio = sample(range(1, 61), 6)
bilhete = ['23','34','3','22','40','50']

print(sorteio, bilhete)
print(set(map(str,sorteio)) & set(bilhete))

