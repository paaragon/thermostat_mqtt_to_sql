import logging
import uuid
import time


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False

# The StreamHandler responsible for displaying
# logs in the console.
sh = logging.StreamHandler()

# Note: the "req_id" param name must be the same as in
# RequestIdFilter.filter
tz = time.strftime('%z')
log_formatter = logging.Formatter(
    fmt="%(asctime)s.%(msecs)03d" + tz +
    " %(levelname)s [%(module)s] %(message).1000s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
sh.setFormatter(log_formatter)
logger.addHandler(sh)
