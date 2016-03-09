# Python 3
import logging
import logging.config
from utils import config
from utils import load

def main():
    # Logging
    logging.config.dictConfig(config.LOG_CONFIG)
    log = logging.getLogger(__name__)
    log.info("Logger initiated")


if __name__ == "__main__":
    print("Project artificial ear")
    main()
