#!/usr/bin/env python3

import check_plants
import data_check
import gen_message
import logging
from notify import send_mail
from datetime import datetime


# Log to a file using logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)


def main() -> dict | None:
    plants = check_plants.check()
    statuses = data_check.check_data(plants)

    if statuses["attention_needed"] is True:
        body = gen_message.generate(statuses)
        # Log mail sent with current date
        logging.info(f"{datetime.now()}: Mail sent")
        return send_mail(body)

    return logging.info(f"{datetime.now()}: No mail sent")


if __name__ == "__main__":
    main()
