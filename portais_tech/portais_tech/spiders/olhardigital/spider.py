import scrapy

from portais_tech.items import PortaisTechItem
from portais_tech.spiders.olhardigital import (get_datetime, get_relacionados,
                                               get_tags, XPATH)


class OlharDigitalSpider(scrapy.Spider):
    name = "olhardigital"

    def start_requests(self):
        url = "https://olhardigital.com.br/"
        yield scrapy.Request(url=url, callback=self.start_site)

    def start_site(self, response):
        url_noticia = response.xpath('//nav[@class="mnu-nav"]/ul/li/'
                                     'a[contains(@href, "noticias")]/'
                                     '@href').extract_first()
        self.log('Extrai url da página de notícias')
        url_noticia = response.urljoin(url_noticia)
        yield scrapy.Request(url=url_noticia, callback=self.extract_links)

    def extract_links(self, response):
        noticias_url = response.xpath('//div[@class="blk-items"]/'
                                      'a/@href').extract()
        self.log(f'A página {response.url} tem {len(noticias_url)} notícias.')

        for noticia in noticias_url:
            url = response.urljoin(noticia)
            yield scrapy.Request(url=url, callback=self.extract_pages_info)

        proxima_pagina = response.xpath('//div[@class="paginacao-rapida"]/'
                                        'a/@href').extract_first()
        if proxima_pagina:
            next_url = response.urljoin(proxima_pagina)
            self.log(f'Faz paginação')
            yield scrapy.Request(url=next_url, callback=self.extract_links)

    def extract_pages_info(self, response):
        self.log(f'Extrai informações da página {response.url}')

        item = PortaisTechItem()
        item['url'] = response.url
        item['titulo'] = response.xpath('//div[@class="hdr-meta"]/'
                                        'h1/text()').extract_first()
        item['autores'] = response.xpath(XPATH.get(
            'info_page').format('meta-aut')).extract_first()
        item['data_publicacao'] = get_datetime(response)
        item['conteudo_relacionado'] = get_relacionados(response)
        item['tags'] = get_tags(response)

        yield item
