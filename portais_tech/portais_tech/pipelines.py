import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class PortaisTechPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem(f"Item perdido {data}!")
        if valid:
            self.collection.insert(dict(item))
            log.msg("Notícia adicionada ao MongoDB dataset!",
                    level=log.DEBUG, spider=spider)
        return item
