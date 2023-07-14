#!/usr/bin/env python3

import check_plants
from notify import send_mail


def main() -> str | dict:
    plants = check_plants.check()

    thirsty = [
        plant for plant in plants
        if plant.get('moisture_status', 0) < 3
        and plant.get("sensor", None) is not None
    ]

    if len(thirsty) > 0:
        if len(thirsty) == 1:
            thirsty_plants = thirsty[0].get('nickname')
        else:
            thirsty_plants = ', '.join([plant.get('nickname') for plant in thirsty])

        body = f'The following plant(s) could use a drink:\n{thirsty_plants}'

        return send_mail(body)

    return 'No plants need watering.'


if __name__ == '__main__':
    main()
