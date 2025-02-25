import logging

logging.basicConfig(filename='papago-deamon.log',
    level=logging.INFO, format='%(asctime)s - %(name)s [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("papago-deamon")