import logging
from logging.config import dictConfig

import os
from redis import StrictRedis, RedisError

from ice_commons.utility.encoding import json_encode, JSONEncoder

from ice_commons.config_settings import app_config
REDIS_URL = app_config['REDIS_END_POINT']

msg_format = '%(levelname)s:%(name)s: (%(lineno)d: %(filename)s): (%(asctime)s);  %(message)s'


def init_logging_dir():
    user_dir = os.path.expanduser('~')
    log_dir = os.path.join(user_dir, '.visualice', 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


def get_log_file():
    user_dir = os.path.expanduser('~')
    log_dir = os.path.join(user_dir, '.visualice', 'logs')
    return os.path.join(log_dir, 'ice.log')


def init_logger():
    logging_config = dict(
        version=1,
        formatters={
            'f': {
                'format': msg_format,
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        handlers={
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG,
            },
            'rotate': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'f',
                'level': logging.DEBUG,
                'filename': get_log_file(),
                'when': 'midnight',
                'backupCount': 3,
                'encoding': 'utf8'
            }
        },
        root={
            'handlers': ['console', 'rotate'],
            'level': logging.DEBUG,
        },
    )

    init_logging_dir()
    dictConfig(logging_config)
    logging.getLogger(__name__).info("Logger initialized successfully!")


class LogArrayHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        logging.Handler.__init__(self, *args, **kwargs)
        self.encoder = JSONEncoder()
        self.logs = []

    def emit(self, record):
        attributes = [
            'name', 'msg', 'levelname', 'levelno', 'pathname', 'filename',
            'module', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated',
            'thread', 'threadName', 'process', 'processName',
        ]
        record_dict = dict((attr, getattr(record, attr)) for attr in attributes)
        record_dict['formatted'] = self.format(record)
        try:
            # self.logs.append(self.encoder.encode(record_dict))
            self.logs.append(json_encode(record_dict))
        except RuntimeError as re:
            logging.getLogger(__name__).exception(re)


class RedisHandler(logging.Handler):
    def __init__(self, channel, conn, *args, **kwargs):
        logging.Handler.__init__(self, *args, **kwargs)
        self.channel = channel
        self.redis_conn = conn
        self.encoder = JSONEncoder()

    def emit(self, record):
        attributes = [
            'name', 'msg', 'levelname', 'levelno', 'pathname', 'filename',
            'module', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated',
            'thread', 'threadName', 'process', 'processName',
        ]
        record_dict = dict((attr, getattr(record, attr)) for attr in attributes)
        record_dict['formatted'] = self.format(record)
        try:
            # self.redis_conn.publish(self.channel, self.encoder.encode(record_dict))
            self.redis_conn.publish(self.channel, json_encode(record_dict))
        except RedisError as re:
            logging.getLogger(__name__).exception(re)


def get_redis_handler(config_id, redis_conn=StrictRedis(REDIS_URL[8:-7], 6379, db=1)):
    handler = RedisHandler(config_id, redis_conn)
    handler.setFormatter(logging.Formatter(msg_format))
    return handler
