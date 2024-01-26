import logging
import sys


def configureLogger():
    """ Configure logger instance """
    logging.basicConfig(
        level=logging.ERROR,
        format='[%(asctime)s][%(levelname)s]: %(message)s',
        stream=sys.stdout
    )

#create and configure Logger
configureLogger()

#get Logger instance
logger = logging.getLogger(__name__)
