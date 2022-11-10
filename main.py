import sys

from utils.Logger import Logger

from configparser import RawConfigParser
from mysql.connector import connect, Error

class Application:
    def __init__(self, config_file):
        self.logger = Logger()
        self.config = RawConfigParser()
        try:
            self.config.read(config_file)
            self.__logger_config__()
            self.connect = self.__db_connect__()
        except Exception as e:
            self.logger.critical('Не удалось прочитать файл с настройками')
            self.logger.critical(e)
            sys.exit()

    def __logger_config__(self):
        config = self.config
        if 'Logger' not in config:
            return
        config = config['Logger']
        str_format = config.get('str_format', None)
        date_format = config.get('date_format', None)
        self.logger.setFormat(str_format, date_format)

    def __db_connect__(self):
        try:
            db_host = self.config['MySQL']['host']
            db_port = int(self.config['MySQL']['port'])
            db_user = self.config['MySQL']['username']
            db_pass = self.config['MySQL']['password']
            with connect(
                host=db_host, user=db_user, password=db_pass,
                port=db_port) as connection:
                self.logger.info('Соединение с базой данных выполнено')
                return connection
        except:
            self.logger.critical('Ошибка соединения с базой данных')


if __name__ == '__main__':
    app = Application('./config.ini')
