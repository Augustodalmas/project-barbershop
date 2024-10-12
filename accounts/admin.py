from django.contrib import admin
from accounts.models import Usuario, Proprietário, Barbeiro


class perfilUsuarioAdministracao(admin.ModelAdmin):
    list_display = ('username', 'data_nascimento', 'numero_telefone')  # Substitua pelos campos reais


class perfilProprietarioAdministracao(admin.ModelAdmin):
    # Substitua pelos campos reais
    list_display = ('propriedade',)


class perfilBarbeiroAdministracao(admin.ModelAdmin):
    list_display = ('cpf',)  # Substitua pelos campos reais


admin.site.register(Usuario, perfilUsuarioAdministracao)
admin.site.register(Proprietário, perfilProprietarioAdministracao)
admin.site.register(Barbeiro, perfilBarbeiroAdministracao)
