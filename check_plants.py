import requests
import config

# TOKEN = getenv('FYTA_TOKEN')
URL = 'https://web.fyta.de/api/user-plant'


def check() -> str | list:
    conf = config.load_conf()
    try:
        token = conf['fyta_auth']['token']
    except KeyError:
        return 'No token detected.'

    # Get plants
    headers = {'Authorization': f'Bearer {token}'}
    plants_request = requests.get(
        url=URL,
        headers=headers
    )
    if plants_request.ok is not True:
        return f'Error {plants_request.status_code} contacting the api:\n' \
               f'{plants_request.text}'

    plants_list = plants_request.json()['plants']

    return plants_list
