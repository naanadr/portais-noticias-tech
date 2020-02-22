import pymongo

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


class PortaisTechPipeline(object):

    def __init__(self):
        settings = get_project_settings()
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
                raise DropItem(f'Item perdido {data}!')
        if valid:
            if item.get('url') in self.collection.distinct('url'):
                raise DropItem(f'Item Duplicado {item.get("url")}')
            else:
                self.collection.insert(dict(item))
        return item
