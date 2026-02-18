from NexusViewPro.logger import logger
from NexusViewPro.custom_exception import InvalidURLException

try:
    raise InvalidURLException()
except Exception as e:
    logger.error(f"An error occurred: {e}")