BOT_NAME = 'portais_tech'

SPIDER_MODULES = ['portais_tech.spiders']
NEWSPIDER_MODULE = 'portais_tech.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Configure item pipelines
ITEM_PIPELINES = {
   'portais_tech.pipelines.MongoPipeline': 500,
   'portais_tech.pipelines.JsonWriterPipeline': 800,

}

MONGO_PORT = 27017
MONGO_SERVER = "db"
MONGO_DATABASE = "portaisnoticias"
