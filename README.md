# portais-noticias-tech [WIP]
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)


Dados obtidos de portais de notícias na área de tecnologia. Foram escolhidos os portais [Olhar Digital](https://olhardigital.com.br/) e [TechTudo](https://www.techtudo.com.br/) como alvos para realizar a extração de notícias relacionadas ao mundo da tecnologia. 


## Índice

* [Como instalar esse projeto?](como-instalar-esse-projeto?)
* [Como executar esse projeto?](como-executar-esse-projeto?)


## Como instalar esse projeto?

Esse projeto possui dois métodos de instalar, o primeiro utilizando um [*enviroment*](#utilizando-um-enviroment) e o segundo utilizando [*docker*](#utilizando-docker).

> Ambos os métodos foram testados em um ambiente linux. Mais especificicamente uma distribuição Manjaro de versão 18.1.5.

## Utilizando um enviroment

1. Instalação do Poetry

Primeiro você precisará instalar o [Poetry](https://python-poetry.org/), o gerenciador de enviroment utilizado nesse projeto. Para isso execute os passos descritos na [documentação](https://python-poetry.org/docs/). 

> A versão utilizada do Poetry foi a 1.0.0

Agora que você instalou o projeto corretamente, execute dentro do diretório principal do projeto (/portais-noticias-tech):

```
$ poetry install --no-dev --no-interaction --no-ansi
```

2. Instalação do MongoDB e do Robo3T

Como nesse projeto persistimos os dados em um bando [MongoDB](https://www.mongodb.com/), você precisará ter ele instalado em sua máquina. Recomendamos utilizar uma imagem docker para isso.

> Caso você não tenha o Docker instalado na sua máquina, esse será o momento de instalar.

```
$ docker pull mongo:latest
$ docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:latest
```

Para visualizar os dados persistidos no MongoDB, você precisará ter o [Robo3T](https://robomongo.org/download) instalado.

> O Snap tem um instalar ótimo do Robo3T, dê uma olhada no [link](https://snapcraft.io/robo3t-snap)

3. Execução do script

Para realizar a extração das notícias você pode executar cada site de notícia por vez:

```
$ scrapy crawl olhardigital
$ scrapy crawl techtudo
```

Ou executar elas de uma vez, utilizando o script `runspiders.py`:

```
$ cd portais_tech
$ python runspiders.py
```

## Utilizando Docker

