#!/usr/bin/env python3

from googleapiclient.discovery import Resource
import check_plants
import config
from notify import send_mail


def main() -> str | dict:
    thirsty = list()
    conf = config.load_conf()
    plants = check_plants.check()
    for plant in plants:
        if plant['moisture_status'] < 3:
            thirsty.append(plant)

    if len(thirsty) > 0:
        if len(thirsty) == 1:
            thirsty_plants = thirsty[0]['nickname']
        else:
            thirsty_plants = ', '.join([plant['nickname'] for plant in thirsty])

        body = f'The following plant(s) could use a drink:\n{thirsty_plants}'

        return send_mail(body)

    return 'No plants need watering.'


if __name__ == '__main__':
    main()
