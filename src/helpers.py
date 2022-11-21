import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def function_from_helpers():
    logger.info("Calling function from helpers")
    return