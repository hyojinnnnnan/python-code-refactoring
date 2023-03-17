from log_refactoring_01.log_01 import write_log as wl01

wl01("wl01 debug test", "debug")
wl01("wl01 info test", "info")
wl01("wl01 warning test", "warning")
wl01("wl01 error test", "error")
wl01("wl01 critical test", "critical")
print("=" * 20)

from log_refactoring_01.log_02 import write_log as wl02

wl02("wl02 debug test", "debug")
wl02("wl02 info test", "info")
wl02("wl02 warning test", "warning")
wl02("wl02 error test", "error")
wl02("wl02 critical test", "critical")
print("=" * 20)

from log_refactoring_01.log_03 import LogLevel, write_log as wl03

wl03("wl03 debug test", LogLevel.DEBUG)
wl03("wl03 info test", LogLevel.INFO)
wl03("wl03 warning test", LogLevel.WARNING)
wl03("wl03 error test", LogLevel.ERROR)
wl03("wl03 critical test", LogLevel.CRITICAL)
print("=" * 20)

import logging
from log_refactoring_01.log_04 import write_log as wl04

wl04("wl04 debug test", logging.DEBUG)
wl04("wl04 info test", logging.INFO)
wl04("wl04 warning test", logging.WARNING)
wl04("wl04 error test", logging.ERROR)
wl04("wl04 critical test", logging.CRITICAL)
print("=" * 20)

from log_refactoring_01.log_05 import write_log as wl05

wl05("wl05 debug test", logging.DEBUG)
wl05("wl05 info test", logging.INFO)
wl05("wl05 warning test", logging.WARNING)
wl05("wl05 error test", logging.ERROR)
wl05("wl05 critical test", logging.CRITICAL)
print("=" * 20)

from log_refactoring_01.log_06 import logger

logger.debug("debug test")
logger.info("info test")
logger.warning("warning test")
logger.error("error test")
logger.critical("critical test")