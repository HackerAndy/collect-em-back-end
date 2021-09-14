import logging
import os

LOG_LEVEL = os.environ.get("LOG_LEVEL", "info")
# Logging Setup
LOG_LEVEL = getattr(logging, LOG_LEVEL.upper(), logging.ERROR)
logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logging.getLogger().setLevel(LOG_LEVEL)
