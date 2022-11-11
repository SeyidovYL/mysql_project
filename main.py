import sys, os

from datetime import datetime
from dynaconf import Dynaconf
from pathlib import PurePath, Path

from utils.Logger import Logger
from mysql.connector import connect, Error


class Application:
    def __init__(self, config_file):
        self.logger = Logger(__name__)
        self.config = Dynaconf(
            settings_file=[config_file],
            environments=False
        )
        try:
            self.__logger_config__(
                self.config.get('Logger', dict())
            )
            self.connect = self.__db_connect__(
                self.config.get('MySQL', dict())
            )
        except Exception as e:
            self.logger.critical('Error', exc_info=True)
            sys.exit()

    def __logger_config__(self, config=dict()):
        curr = Path(__file__).parent.resolve()
        path = config.get('path', None)
        if path:
            curr = PurePath(curr, path)
        filename = config.get('filename', None)
        if filename:
            filename = datetime.now().strftime(filename)
            filename = PurePath(curr, filename)
            try:
                os.makedirs(curr, mode=0o755, exist_ok=True)
            except:
                filename = None
        self.logger.format_date = config.get('format_date', None)
        self.logger.format_message = config.get('format_message', None)
        self.logger.filename = filename
    def __db_connect__(self, config=dict()):
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
