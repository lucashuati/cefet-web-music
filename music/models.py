from django.db import models

class Banda(models.Model):
    nome = models.TextField()
    cover = models.BooleanField()
    fundacao = models.DateField()
    estilo = models.ForeignKey('EstiloMusical', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Musico(models.Model):
    nome = models.TextField()
    idade = models.IntegerField()
    bandas = models.ManyToManyField(Banda, related_name='musicos')
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class EstiloMusical(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome
