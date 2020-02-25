import scrapy
from scrapy.loader import ItemLoader

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
                                     '@href').get()
        self.log('Extrai url da página de notícias')
        url_noticia = response.urljoin(url_noticia)
        yield scrapy.Request(url=url_noticia, callback=self.extract_links)

    def extract_links(self, response):
        noticias_url = response.xpath('//div[@class="blk-items"]/'
                                      'a/@href').getall()
        self.log(f'A página {response.url} tem {len(noticias_url)} notícias.')

        for noticia in noticias_url:
            url = response.urljoin(noticia)

            meta = response.meta
            meta['callback'] = 'extract_pages_info'

            yield scrapy.Request(url=url, meta=meta,
                                 callback=self.extract_pages_info)

        proxima_pagina = response.xpath('//div[@class="paginacao-rapida"]/'
                                        'a[@class="btn-prx"]/'
                                        '@href').get()
        if proxima_pagina:
            next_url = response.urljoin(proxima_pagina)
            self.log(f'Faz paginação da página {response.url} para {next_url}')
            yield scrapy.Request(url=next_url, callback=self.extract_links)

    def extract_pages_info(self, response):
        self.log(f'Extrai informações da página {response.url}')

        loader = ItemLoader(item=PortaisTechItem(), response=response)
        loader.add_value('spider', self.name)
        loader.add_value('url', response.url)
        loader.add_xpath('titulo', '//div[@class="hdr-meta"]/h1/text()')
        loader.add_xpath('autor', XPATH.get('info_page').format('meta-aut'))
        loader.add_value('data_publicacao', get_datetime(response))
        loader.add_value('conteudo_relacionado', get_relacionados(response))
        loader.add_value('tags', get_tags(response))
        loader.add_xpath('referencias', '//em/a[@target="_blank"]/@href')

        if (', ' in response.xpath(XPATH.get('info_page').format(
                'meta-aut')).get()):
            loader.add_xpath('revisor', XPATH.get('info_page').format(
                'meta-aut'))

        # TODO - Corrigir xpath da captura de comentários
        #loader.add_xpath('qtd_comentarios', '//span/span[@class=" _50f7"]/'
        #                                    'text()')

        yield loader.load_item()
