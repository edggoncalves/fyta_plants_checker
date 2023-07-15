#!/usr/bin/env python3

import check_plants
import data_check
import gen_message
import logging
from os import path
from notify import send_mail
from datetime import datetime

# Find local path
local_path = path.dirname(path.abspath(__file__))
# Log to a file using logging
logging.basicConfig(filename=f"{local_path}/logs/log.txt", level=logging.DEBUG)


def main() -> dict | None:
    plants = check_plants.check()
    print("Got plants")
    statuses = data_check.check_data(plants)
    print("Got statuses")

    if statuses["attention_needed"] is True:
        body = gen_message.generate(statuses)
        print("Generating and sending email")
        # Log mail sent with current date
        logging.info(f"{datetime.now()}: Mail sent")
        return send_mail(body)

    print("Sleeping")
    return logging.info(f"{datetime.now()}: No mail sent")


if __name__ == "__main__":
    main()
