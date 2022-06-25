import datetime
import time
import traceback
from typing import Optional
from typing import Tuple

import psutil
import requests

from discord_status_changer import config
from discord_status_changer.logger import get_logger

logger = get_logger("status", split=" ")


def get_process_quote() -> Optional[str]:
    """
    If any process of `config.PROCESS` is running returns
    specified quote otherwise returns None
    """
    for proc in psutil.process_iter():
        try:
            name = proc.name()
            if name in config.PROCESS:
                return config.PROCESS[name]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None


def get_daily_quote() -> Tuple[str, str]:
    """
    Gets quote of the day
    """
    days = (datetime.datetime.now().date() - datetime.datetime(1970, 1, 1).date()).days
    return config.QUOTES[days % len(config.QUOTES)]


def get_quote() -> dict:
    """
    Gets quote for showing in discord
    """
    q = get_process_quote()
    if q is None:
        q = get_daily_quote()
        text = q
        emoji = None
    else:
        text = q[0]
        emoji = q[1]
    return {"custom_status": {"text": text, "emoji_name": emoji}}


def main():
    logger.info("Start status changer")
    last_payload = None
    error_cnt = 0
    while error_cnt < config.MAX_ERROR:
        payload = get_quote()
        if str(last_payload) != str(payload):
            logger.info("New payload %s", payload)
            try:
                response = requests.request(
                    "PATCH", config.URL, json=payload, headers=config.HEADERS
                )
                last_payload = payload
                logger.info("Status code %d", response.status_code)
            except ConnectionError as e:
                logger.error("Connection error")
                time.sleep(60)
            except Exception as e:
                error_cnt += 1
                logger.error(
                    "Failed to change status %s\n%s", e, traceback.format_exc()
                )
                time.sleep(60)
        time.sleep(60)

    logger.error("MAX_ERROR exceeded")


if __name__ == "__main__":
    main()
