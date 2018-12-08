from django.forms import ModelForm
from .models import Pessoa

class createPessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['pe_nome', 'pe_sobrenome', 'pe_idade', 'pe_salario', 'pe_bio', 'pe_foto']
