# README

Este script normaliza os dados brutos das eleições 2014 (1o. Turno) que
aconteceu no dia 5 de Outubro de 2014.

## Importação dos dados

Por padrão utilizamos sqlite salvo no `/tmp/`. Aconselha-se o uso do file
system `tmpfs` para melhorar o tempo de importação.

Caso queira mudar o backend da base de dados, ou o local do mesmo, por favor,
altere o arquivo `eleicoes2014/settings.py`.

Sincronize o banco:

```bash
$ python manage.py syncdb
```

Inicie a importação:

```bash
$ export PYTHONPATH=.:$PYTHONPATH
$ export DJANGO_SETTINGS_MODULE=eleicoes2014.settings
$ python utils/import.py
```

NOTA: Salve e descompacte os arquivos dos [Boletem de
Urna](http://www.tse.jus.br/hotSites/pesquisas-eleitorais/resultados_anos/boletim_urna/boletim_urna_1_turno-2014.html)
do TSE no diretório `raw` antes de executar o script.

## Acesse a base normalizada

```bash
$ ipython

In [1]: from core.models import *                                
In [2]: for bu in BU.objects.all():                               
    print bu.votavel.numero, bu.votavel.nome, bu.votavel.cargo.descricao, bu.votos
```

## Autores

  * Beraldo Leal <beraldo AT ime DOT usp DOT br>
