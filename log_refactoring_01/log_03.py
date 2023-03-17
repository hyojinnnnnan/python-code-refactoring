""" Refactoring Point : log_02 > log_03
Enum 사용
  - 문자열을 전달하여 발생하는 실수 예방
    - [중요] p_log_type (로그의 레벨: debug, info...) 문자열을 잘못 전달했을 때 오류가 발생하지 않는 문제 해결
  - Enum으로 전달하는 파라메터의 종류 제한
  - Enum의 value를 통해 로그 레벨 비교
"""
import time
from logging.config import dictConfig
import logging
from enum import Enum

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


# enum 클래스 정의 : enum 내장 모듈로 부터 불러온 Enum 클래스를 확장하여 LogLevel 타입 생성
class LogLevel(Enum):
  """
  Logging level
  """
  # enum 타입의 상수 인스턴스는 기본적으로 이름(name)과 값(value)을 속성을 가짐
  INFO = 20
  WARNING = 30
  ERROR = 40
  CRITICAL = 50
  DEBUG = 10


# Enum으로 전달하는 p_log_type의 파라메터의 종류 제한
def write_log(p_log_msg: str, p_log_type: LogLevel):
  log_level_map = {
    LogLevel.INFO: logging.info,
    LogLevel.WARNING: logging.warning,
    LogLevel.ERROR: logging.error,
    LogLevel.CRITICAL: logging.critical,
    LogLevel.DEBUG: logging.debug
  }

  log_level_map[p_log_type](p_log_msg)
  if p_log_type.value > LogLevel.DEBUG.value:  # Enum의 value를 통해 로그 레벨 비교
    return print(p_log_msg)


""" write_log("debug test", "debug") : 
p_log_type 에 대해 문자열로 흐름을 제어하고, 
문자열을 잘못 전달했을 때 오류가 발생하지 않는 문제 해결

Traceback (most recent call last):
  File "main.py", line 19, in <module>
    wl03("debug test", "debug")
  File "/home/runner/pythoncoderefactoring/log_refactoring_01/log_03.py", line 57, in write_log
    log_level_map[p_log_type](p_log_msg)
KeyError: 'debug'
"""
