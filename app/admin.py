from django.contrib import admin

# Register your models here.
from .models import NFCe
from .models import Tabelaexternareferenciada

admin.site.register(NFCe)
admin.site.register(Tabelaexternareferenciada)
