import pymongo

from scrapy import signals
from scrapy.exceptions import IgnoreRequest


class PortaisTechDownloaderMiddleware(object):
    urls_distinct = set()

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)

        s.mongo_connection(crawler)
        s.add_urls()

        return s

    def mongo_connection(self, crawler):
        mongo_server = crawler.settings.get('MONGO_SERVER'),
        mongo_port = crawler.settings.get('MONGO_PORT'),
        mongo_db = crawler.settings.get('MONGO_DATABASE')
        self.mongo_collection = crawler.settings.get('MONGO_COLLECTION'),

        self.client = pymongo.MongoClient(mongo_server, mongo_port)
        self.db = self.client[mongo_db]

    def add_urls(self):
        collection = self.db[self.mongo_collection]

        for numero in collection.aggregate([{'$group': {'_id': '$url'}}]):
            self.urls_distinct.add(numero['_id'])

    def process_request(self, request, spider):
        url = request.url

        if url in self.urls_distinct:
            raise IgnoreRequest(f'Request ignorada. Url {url} já foi '
                                f'utilizada')

        self.urls_distinct.add(url)
        return None

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
