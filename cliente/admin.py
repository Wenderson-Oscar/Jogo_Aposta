from django.contrib import admin
from .models import Cliente, Carteira, MegaSena, JogoBicho, PremiuBicho, BilheteClienteLoteria

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Carteira)
admin.site.register(MegaSena)
admin.site.register(JogoBicho)
admin.site.register(PremiuBicho)
admin.site.register(BilheteClienteLoteria)