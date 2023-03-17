""" Refactoring Point : log_01 > log_02
if-else 대신 dict 사용
  - 단순 함수 매핑 용도는 dict를 사용하는 것이 가독성이 좋음
  - 함수 자체를 value로 정하여 가져와서 추후 호출할 수 있음
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


# 콘솔 로그 출력, 로그 파일 기록
def write_log(p_log_msg, p_log_type):
  log_msg = p_log_msg

  # if-else 대신 dict 사용 : 단순 함수 매핑 용도는 dict를 사용
  log_level_map = {
    "info": {
      "logging_function": logging.info,  # 함수 자체를 value로 정하여 가져와서 추후 호출할 수 있음
      "logging_level": 20
    },
    "warning": {
      "logging_function": logging.warning,
      "logging_level": 30
    },
    "error": {
      "logging_function": logging.error,
      "logging_level": 40
    },
    "critical": {
      "logging_function": logging.critical,
      "logging_level": 50
    },
    "debug": {
      "logging_function": logging.debug,
      "logging_level": 10
    }
  }

  log_level_map[p_log_type]["logging_function"](log_msg)
  # ex) logging.info(log_msg) ~ p_log_type에 맞는 로깅 함수 호출

  # info 레벨 이후부터 콘솔 출력
  if log_level_map[p_log_type]["logging_level"] > 10:
    print(log_msg)