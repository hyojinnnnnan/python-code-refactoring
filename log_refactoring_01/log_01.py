import time
from logging.config import dictConfig
import logging

####################################################################
# 디버깅용 로그 : from logging.config import dictConfig
####################################################################
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
            'filename': './log/'+time.strftime('%y%m%d')+'_debug.log',
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
    """
    p_log_type (log_level) : debug(10), info(20), warning(30), error(40), critical(50)
    >> log_level > 10 : return print(log_msg)
    """
    log_msg = p_log_msg

    if p_log_type == "info":
        # 2단계 INFO: 일반 정보
        logging.info(log_msg)
        log_level = 20
    elif p_log_type == "warning":
        # 3단계 WARNING: 경고 정보(작은 문제)
        logging.warning(log_msg)
        log_level = 30
    elif p_log_type == "error":
        # 4단계 ERROR: 오류 정보(큰 문제)
        logging.error(log_msg)
        log_level = 40
    elif p_log_type == "critical":
        # 5단계 CRITICAL: 아주 심각한 문제
        logging.critical(log_msg)
        log_level = 50
    else:
        # 1단계 DEBUG: 디버깅 목적
        logging.debug(log_msg)
        log_level = 10

    # INFO 이후 부터 콘솔 출력
    if log_level > 10:
        return print(log_msg)