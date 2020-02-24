import pymongo

from scrapy.exceptions import DropItem


class MongoPipeline(object):

    collection_name = 'tech'

    def __init__(self, mongo_server, mongo_port, mongo_db):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGO_SERVER'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[self.collection_name]
        for data in item:
            if not data:
                raise DropItem(f'Item perdido {data}!')
        else:
            if item.get('url') in collection.distinct('url'):
                raise DropItem(f'Item Duplicado {item.get("url")}')
            else:
                collection.insert(dict(item))
        return item
