import logging
import sys

def configureLogger():
    logging.basicConfig(
        level=logging.ERROR,
        format='[%(asctime)s][%(levelname)s]: %(message)s',
        stream=sys.stdout
    )

# Create and configure the logger
configureLogger()

# Get the logger instance
logger = logging.getLogger(__name__)
