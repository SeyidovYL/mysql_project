from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')

db_host = config['MySQL']['host']
db_port = int(config['MySQL']['port'])
db_user = config['MySQL']['username']
db_pass = config['MySQL']['password']
