class BaseConfig:
    """
    cassandra configuration
    """

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    port = 8080


config = {
    'development': DevelopmentConfig
}
