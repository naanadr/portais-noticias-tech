import scrapy


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
            # TODO

        proxima_pagina = response.xpath('//div[@class="paginacao-rapida"]/'
                                        'a/@href').extract_first()
        if proxima_pagina:
            next_url = response.urljoin(proxima_pagina)
            self.log(f'Faz paginação')
            yield scrapy.Request(url=next_url, callback=self.extract_links)
