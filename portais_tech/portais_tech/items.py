import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def get_autor(value):
    editado_msg = ','
    if editado_msg in value:
        value = value.split(editado_msg)[0]

    return value


def get_revisor(value):
    editado_msg = ' por '
    if editado_msg in value:
        value = value.split(editado_msg)[1]

    return value


def qtd_comentarios(value):
    if 'comentários' in value:
        value = value.split(' ')[0]

    return int(value)


class PortaisTechItem(scrapy.Item):
    spider = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    url = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    titulo = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    qtd_comentarios = scrapy.Field(
        input_processor=MapCompose(qtd_comentarios),
        output_processor=TakeFirst(),
    )
    autor = scrapy.Field(
        input_processor=MapCompose(get_autor),
        output_processor=TakeFirst(),
    )
    revisor = scrapy.Field(
        input_processor=MapCompose(get_revisor),
        output_processor=TakeFirst(),
    )
    data_publicacao = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    referencias = scrapy.Field()
    conteudo_relacionado = scrapy.Field(
        input_processor=MapCompose(get_revisor),
    )
    tags = scrapy.Field()
