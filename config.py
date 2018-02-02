import ssl
import logging
from logstash_formatter import LogstashFormatterV1

class BaseConfig:
    """
    cassandra configuration
    """

    CASSANDRA_HOSTS = ['cassandra']
    CASSANDRA_KEYSPACE = 'cqlengine'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    port = 8080


class ProductionConfig(BaseConfig):
    ssl_options = {
                      'ca_certs': './certs/rootCa.crt',
                      'ssl_version': ssl.PROTOCOL_TLSv1
                  }
    # Setting cassandra args for ssl_options
    CASSANDRA_SETUP_KWARGS = {
        'ssl_options': ssl_options
    }


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


class Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = LogstashFormatterV1()

    file_handler = logging.FileHandler('APILogger.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler) 
                
