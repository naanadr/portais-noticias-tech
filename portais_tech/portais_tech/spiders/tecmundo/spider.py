import scrapy
from scrapy.loader import ItemLoader

from portais_tech.items import PortaisTechItem
from portais_tech.spiders.tecmundo import get_datetime


class TecMundoSpider(scrapy.Spider):
    name = "tecmundo"

    def start_requests(self):
        url = "https://www.tecmundo.com.br"
        yield scrapy.Request(url=url, callback=self.start_site)

    def start_site(self, response):
        """
         No site do TecMundo tem algumas categorias que não relevantes para as
         análises futuras, são elas:
            * Udemy
            * Comparar Celulares
            * Cupons de Desconto
            * Teste de Velocidade

          Por isso elas serão removidas do fluxo, inserindo o [:-3] ao fim do
          `getall()`.
        """
        categorias = response.xpath('//ul[contains(@class, '
                                    '"nav--horizontal")]/li/'
                                    'a[@class="tec--nav__link"]/'
                                    '@href').getall()[:-3]

        for categoria in categorias:
            categoria = response.urljoin(categoria)

            yield scrapy.Request(url=categoria,
                                 callback=self.extract_links)

    def extract_links(self, response):
        noticias = response.xpath('//h3/a[contains(@class, "title__link")]/'
                                  '@href').getall()

        self.log(f'A página {response.url} tem {len(noticias)} notícias.')

        for noticia in noticias:
            yield scrapy.Request(url=noticia, callback=self.extract_pages_info)

        self.paginacao(response)

    def paginacao(self, response):
        next_page = response.xpath('//a[contains(@class, '
                                   '"tec--btn tec--btn--lg")]/@href').get()

        if next_page:
            self.log(f'Faz paginação da página {response.url} para'
                     f' {next_page}')
            yield scrapy.Request(url=next_page, callback=self.extract_links)

    def extract_pages_info(self, response):
        self.log(f'Extrai informações da página {response.url}')

        loader = ItemLoader(item=PortaisTechItem(), response=response)
        loader.add_value('spider', self.name)
        loader.add_value('url', response.url)
        loader.add_xpath('titulo', '//h1[contains(@class, '
                         '"header__title")]/text()')
        loader.add_xpath('autor', '//div[contains(@class, "author")]/p/a/'
                                  'text()')
        loader.add_value('data_publicacao', get_datetime(response))
        loader.add_xpath('referencias', '//a[@class="tec--badge"]/@href')
        loader.add_xpath('conteudo_relacionado', '//div[contains(@class, '
                         '"__body")]/*/*[self::p or self::li]/'
                         'a[@target="_blank"]/@href')
        loader.add_xpath('tags', '//div[@id="js-categories"]/a/text()')
        loader.add_xpath('qtd_comentarios', '//button[@id="js-comments-btn"]/'
                                            '@data-count')
        yield loader.load_item()
