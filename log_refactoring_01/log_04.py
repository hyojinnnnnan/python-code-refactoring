""" Refactoring Point : log_03 > log_04
logging에서 제공하는 log_level 활용
    - logging.DEBUG 자체가 정수형으로 크기 비교가 가능함을 활용
      - log_03 처럼 enum 클래스를 정의할 필요가 없어짐
"""
import time
from logging.config import dictConfig
import logging

dictConfig({
  'version': 1,
  'formatters': {
    'default': {
      'format': '[%(asctime)s] %(message)s',
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
  log_level_map = {
    logging.INFO: logging.info,
    logging.WARNING: logging.warning,
    logging.ERROR: logging.error,
    logging.CRITICAL: logging.critical,
    logging.DEBUG: logging.debug
  }
  """
  print(logging.INFO)  # 20
  print(type(logging.INFO))  # <class 'int'>
  print(type(logging.info))  # <class 'function'>
  """
  log_level_map[p_log_type](p_log_msg)
  if p_log_type > logging.DEBUG:
    print(p_log_msg)