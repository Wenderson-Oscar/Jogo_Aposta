from django.contrib import admin
from .models import Cliente, Carteira, MegaSena

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Carteira)
admin.site.register(MegaSena)