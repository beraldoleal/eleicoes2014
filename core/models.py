from django.db import models

# Create your models here.

class Estado(models.Model):
    sigla = models.CharField(max_length=2)

class Municipio(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado)

class Local(models.Model):
    codigo = models.IntegerField()
    municipio = models.ForeignKey(Municipio)

class Zona(models.Model):
    codigo = models.IntegerField()
    local = models.ForeignKey(Local)

class Secao(models.Model):
    codigo = models.IntegerField()
    zona = models.ForeignKey(Zona)

class Cargo(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=255)

class Partido(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=255)

class TipoUrna(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=255)

class Urna(models.Model):
    codigo = models.IntegerField()
    tipo = models.ForeignKey(TipoUrna)
    secao = models.ForeignKey(Secao)
    carga_1 = models.CharField(max_length=255)
    carga_2 = models.CharField(max_length=255)
    flashcard = models.CharField(max_length=255)
    aptos = models.IntegerField()
    faltosos = models.IntegerField()
    presentes = models.IntegerField()

class Votavel(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=255)
    partido = models.ForeignKey(Partido)
    cargo = models.ForeignKey(Cargo)
#    tipo = models.CharField(max_length=255)

class BU(models.Model):
#    gerado = models.DateTime()
#    recebido = models.DateTime()
#    codigo_pleito = models.IntegerField()
#    codigo_eleicao = models.IntegerField()
#    tipo_eleicao = models.IntegerField()

    urna = models.ForeignKey(Urna)
    votavel = models.ForeignKey(Votavel)
    votos = models.BigIntegerField()
