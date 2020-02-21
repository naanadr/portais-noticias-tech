from scrapy.item import Item, Field


class PortaisTechItem(Item):
    url = Field()
    titulo = Field()
    autores = Field()
    data_publicacao = Field()
    conteudo_relacionado = Field()
    tags = Field()
