#!/usr/bin/env python

from core.models import *
import os

fields = (
"data_geracao",
"hora_geracao",
"codigo_pleito",
"codigo_eleicao",
"sigla_uf",
"codigo_cargo",
"descricao_cargo",
"zona_eleitoral",
"secao_eleitoral",
"local_votacao",
"numero_partido",
"nome_partido",
"codigo_municipio",
"nome_municipio",
"data_bu_recebido",
"aptos",
"faltosos",
"presentes",
"codigo_tipo_eleicao",
"tipo_urna",
"tipo_urna_descricao",
"numero_votavel",
"nome_votavel",
"votos",
"tipo_votavel",
"numero_urna_efetivada",
"carga_1",
"carga_2",
"flashcard",
"cargo_pergunta_secao",
)

def _(field):
    return fields.index(field)

for file in os.listdir("raw/"):
    if file.endswith(".txt"):
        with open("raw/%s" % file, 'r') as f:
            for line in f:
              splited = line.replace('\"','').decode('iso-8859-1').split(";")
              estado, c = Estado.objects.get_or_create(sigla = splited[_('sigla_uf')])
              municipio, c = Municipio.objects.get_or_create(codigo = int(splited[_('codigo_municipio')]),
                                                             nome = splited[_('nome_municipio')],
                                                             estado = estado)
              local, c = Local.objects.get_or_create(codigo = int(splited[_('local_votacao')]),
                                                     municipio = municipio)
              zona, c = Zona.objects.get_or_create(codigo = int(splited[_('zona_eleitoral')]),
                                                   local = local)
              secao, c = Secao.objects.get_or_create(codigo = int(splited[_('secao_eleitoral')]),
                                                     zona = zona)
              cargo, c = Cargo.objects.get_or_create(codigo = int(splited[_('codigo_cargo')]),
                                                     descricao = splited[_('descricao_cargo')])
              partido, c = Partido.objects.get_or_create(numero = int(splited[_('numero_partido')]),
                                                         nome = splited[_('nome_partido')])
              votavel, c = Votavel.objects.get_or_create(numero = int(splited[_('numero_votavel')]),
                                                         nome = splited[_('nome_votavel')],
                                                         partido = partido,
                                                         cargo = cargo)
          #                                               tipo = splited[_('tipo_votavel')])
              tipo_urna, c = TipoUrna.objects.get_or_create(codigo = int(splited[_('tipo_urna')]),
                                                            descricao = splited[_('tipo_urna_descricao')])
              urna, c = Urna.objects.get_or_create(codigo = int(splited[_('numero_urna_efetivada')]),
                                                   tipo = tipo_urna,
                                                   secao = secao,
                                                   carga_1 = splited[_('carga_1')],
                                                   carga_2 = splited[_('carga_2')],
                                                   flashcard = splited[_('flashcard')],
                                                   aptos = int(splited[_('aptos')]),
                                                   faltosos = int(splited[_('faltosos')]),
                                                   presentes = int(splited[_('presentes')]))
              bu = BU(urna = urna,
                      votavel = votavel,
                      votos = int(splited[_('votos')]))
              bu.save()
              print bu.urna.codigo, \
                    bu.urna.secao.codigo, \
                    bu.urna.secao.zona.codigo, \
                    bu.votavel.nome, \
                    bu.votos
