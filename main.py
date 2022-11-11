import sys

from dynaconf import Dynaconf
from utils.Logger import Logger
from mysql.connector import connect, Error


class Application:
    def __init__(self, config_file):
        self.config = Dynaconf(
            settings_file=[config_file],
            environments=False
        )
        logger_config = self.config.get('Logger')
        self.logger = Logger(logger_config)
        try:
            self.connect = self.__db_connect__(
                self.config.get('MySQL', dict())
            )
        except Exception as e:
            self.logger.exception(e)
            sys.exit()

    def __db_connect__(self, config=None):
        if not config:
            raise Exception('Не найдена конфигурация базы данных')
        db_host = config.get('host')
        db_port = int(config.get('port'))
        db_user = config.get('username')
        db_pass = config.get('password')
        with connect(
            host=db_host, user=db_user, password=db_pass,
            port=db_port
        ) as connection:
            self.logger.info('Соединение с базой данных выполнено')
            return connection


if __name__ == '__main__':
    app = Application('./config.json')
