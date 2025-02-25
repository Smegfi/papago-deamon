import requests
import threading
import schedule
from logger import logger
from config import Config
import time


def runJob():
    logger.info("Sending request to papago-app server...")
    try:
        config = Config()
        response = requests.get(config.API_URL, timeout=config.TIMEOUT, verify=False)
        logger.info(f'Response from papago-app server code:{response.status_code} message:{response.text}')

    except ValueError as e:
        logger.error(f"Environment variables are not set. Error: {e}")
    except Exception as e:
        logger.error(f"Papago-app server did not respond. Error: {e}")

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(10).seconds.do(run_threaded, runJob)

if __name__ == "__main__":
    logger.info('starting papago-deamon...')
    while True:
        schedule.run_pending()
        time.sleep(1)
    logger.info('papago-demaon exited...')