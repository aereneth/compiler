class Config(object):
    DEBUG = True
    SECRET_KEY = '\x1d\xd8\xbbbd=\xd2u\\\xeeY\xc1IY\x18\x84<\xd1w\xce\xea\x01\x07u'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = True