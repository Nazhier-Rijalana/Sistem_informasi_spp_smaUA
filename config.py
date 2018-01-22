class Config(object):

class DevelopmentConfig(Config):
	DEBUG = True
	CSRF_ENABLED = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	DEBUG = False
	CSRF_ENABLED = True
	SQLALCHEMY_ECHO = False

app_config = {
	'dev' : DevelopmentConfig,
	'pro' : ProductionConfig
}