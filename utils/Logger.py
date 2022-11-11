import logging

class Logger:
    __config={
        'level': logging.DEBUG,
        'format': None,
        'datefmt': None,
        'filename': None
    }

    def __init__(self, name='logger'):
        self.logger = logging.getLogger(name)
        self.__reconf__()

    def __reconf__(self):
        self.logger.setLevel(self.__config.get('level'))
        for hdlr in self.logger.handlers[:]:
            self.logger.removeHandler(hdlr)
        if self.filename:
            fileh = logging.FileHandler(self.filename, 'a')
            formatter = logging.Formatter(self.format_message)
            fileh.setFormatter(formatter)
            self.logger.addHandler(fileh)

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

    @property
    def format_message(self):
        return self.__config.get('format')

    @format_message.setter
    def format_message(self, value=None):
        self.__config['format'] = value
        self.__reconf__()

    @property
    def format_date(self):
        return self.__config.get('datefmt')

    @format_date.setter
    def format_date(self, value=None):
        self.__config['datefmt'] = value
        self.__reconf__()

    @property
    def filename(self):
        return self.__config.get('filename')

    @filename.setter
    def filename(self, value=None):
        self.__config['filename'] = value
        self.__reconf__()
