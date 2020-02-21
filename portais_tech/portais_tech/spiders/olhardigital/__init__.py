from datetime import datetime


XPATH = {
    'info_page': ('//div[@class="mat-meta"]/span[contains(@class, "{}")]'
                  '/text()'),
}


def get_datetime(response):
    data = response.xpath(XPATH.get('info_page').format(
        'meta-pub-d')).extract_first()
    hora = response.xpath(XPATH.get('info_page').format(
        'meta-pub-h')).extract_first()

    hora = hora.replace('h', ':')
    data_hora = f'{data} {hora}:00'
    data_hora = datetime.strptime(data_hora, '%d/%m/%Y %H:%M:%S')
    return data_hora


def get_relacionados(response):
    relacionados = response.xpath('//div[@class="mat-txt-links"]/'
                                  'a/@href').extract()
    relacionados = [response.urljoin(rel) for rel in relacionados]

    return relacionados


def get_tags(response):
    tags = response.xpath('//div[@class="mat-tags"]/span/text()').extract()
    tags = [t.lower() for t in tags]

    return tags
