from django.db import models

class Pessoa(models.Model):
    pe_nome = models.CharField(max_length=50)
    pe_sobrenome = models.CharField(max_length=50)
    pe_idade = models.PositiveIntegerField()
    pe_salario = models.DecimalField(max_digits=5, decimal_places=2)
    pe_bio = models.TextField()
    pe_foto = models.ImageField(upload_to='foto_cliente', null=True, blank=True)

    def __str__(self):
        return self.pe_nome + ' ' + self.pe_sobrenome
