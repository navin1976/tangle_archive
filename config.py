import logging
from logstash_formatter import LogstashFormatterV1

class BaseConfig:
    """
    cassandra configuration
    """

    CASSANDRA_HOSTS = ['127.0.0.1']
    CASSANDRA_KEYSPACE = 'cqlengine'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    port = 9080


config = {
    'development': DevelopmentConfig
}

class Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = LogstashFormatterV1()

    file_handler = logging.FileHandler('APILogger.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler) 
                
