import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.DEBUG)
        self.file_handler = None

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def setFormat(self, str_format=None, date_format=None):
        config = dict()
        if str_format:
            config['format'] = str_format
        if date_format:
            config['datefmt'] = date_format
        logging.basicConfig(**config)

