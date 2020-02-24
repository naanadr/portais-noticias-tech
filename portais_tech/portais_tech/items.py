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


class PortaisTechItem(scrapy.Item):
    url = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    titulo = scrapy.Field(
        input_processor=TakeFirst(),
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
    conteudo_relacionado = scrapy.Field(
        input_processor=MapCompose(get_revisor),
    )
    tags = scrapy.Field()
