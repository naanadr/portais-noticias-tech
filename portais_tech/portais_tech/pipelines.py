import datetime
import json
import os
import pymongo

from scrapy.exceptions import DropItem


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        if not bool(int(os.environ['USE_JSON'])):
            self.file = None
        else:
            self.file = open(f'./{spider.name}.jl', 'a+')

    def close_spider(self, spider):
        if not bool(int(os.environ['USE_JSON'])):
            self.file = None
        else:
            self.file.close()

    def process_item(self, item, spider):
        if not bool(int(os.environ['USE_JSON'])):
            return None

        item = dict(item)
        if (isinstance(item.get('data_publicacao'),
                       (datetime.date, datetime.datetime))):
            item['data_publicacao'] = item.get('data_publicacao').isoformat()

        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class MongoPipeline(object):

    mongo_collection = 'tech'

    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_collection):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGO_SERVER'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[self.mongo_collection]
        for data in item:
            if not data:
                raise DropItem(f'Item perdido {data}!')
        else:
            distintos = set()
            for numero in collection.aggregate([{'$group': {'_id': '$url'}}]):
                distintos.add(numero['_id'])

            if item.get('url') in distintos:
                raise DropItem(f'Item Duplicado {item.get("url")}')
            else:
                collection.insert(dict(item))
        return item
