""" Refactoring Point : log_04 > log_05
logging에서 제공하는 log 함수 활용
  - log level을 파라미터로 받아서 level에 따라 동작하는 함수 사용
"""
import time
from logging.config import dictConfig
import logging

dictConfig({
  'version': 1,
  'formatters': {
    'default': {
      'format': '%(asctime)s - %(levelname)s - %(message)s',
    }
  },
  'handlers': {
    'file': {
      'level': 'DEBUG',
      'class': 'logging.FileHandler',
      'filename': './log/' + time.strftime('%y%m%d') + '_debug.log',
      'formatter': 'default',
    },
  },
  'root': {
    'level': 'DEBUG',
    'handlers': ['file']
  }
})


def write_log(p_log_msg: str, p_log_type: int):
  logging.log(p_log_type, p_log_msg)
  if p_log_type > logging.DEBUG:
    print(p_log_msg)
