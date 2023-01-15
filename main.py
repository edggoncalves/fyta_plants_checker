#!/usr/bin/env python3

from googleapiclient.discovery import Resource
import check_plants
import config
from notify import send_mail


def main() -> str | Resource:
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

        return send_mail(
            destination=conf['email_config']['to'],
            subject='Your plants need attention!',
            text=f'The following plant(s) could use a drink:\n'
                 f'{thirsty_plants}'
        )

    return 'No plants need watering.'


if __name__ == '__main__':
    main()
