""" Refactoring Point : log_05 > log_06
logging에서 제공하는 log 로직 활용
  - logging.config에서 아래와 같은 설정이 모두 가능
    - log level에 따른 동작
    - 출력 포인트 설정
    - 출력 포맷에 log_level도 표시되도록 수정
    - log rotation 적용
  - 로그 filename에 f-string 적용
"""

import logging
from logging.config import dictConfig
import time

dictConfig({
  'version': 1,

  'formatters': {
    'default': {
      "format":
      "[%(asctime)s] %(levelname)s : %(message)s",  # 출력 포맷에 log_level도 표시되도록 수정
      "datefmt": "%Y-%m-%d %H:%M:%S",
    }
  },

  'handlers': { # log level에 따른 동작
    'console': { # 콘솔에서는 info 레벨부터 출력
      'level': 'INFO',
      'class': 'logging.StreamHandler',
      'formatter': 'default',
      'stream': 'ext://sys.stdout',
    },
    'file': { # log 파일에는 debug 레벨부터 모두 기록
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler', # File size 기반 rotating logs 적용
      'filename':  # 로그 filename에 f-string 적용
      f'./log/{time.strftime("%y%m%d")}.log',
      'formatter': 'default',
      'maxBytes': 1024 * 10,
      'backupCount': 5,
    },
  },

  'loggers': {
    'debug': {
      'level': 'INFO',
      'handlers': ['console'],
      'propagate': False,
    }
  },

  'root': {
    'level': 'DEBUG',
    'handlers': ['file', 'console']
  }
})

logger = logging.getLogger()