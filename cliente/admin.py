from django.contrib import admin
from .models import Cliente, Carteira, MegaSena, JogoBicho

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Carteira)
admin.site.register(MegaSena)
admin.site.register(JogoBicho)