import requests
import config
from immutables import URL


def check() -> list:
    conf = config.load_conf()
    try:
        token = conf["fyta_auth"]["token"]
    except KeyError:
        raise KeyError(f"No token detected.")

    # Get plants
    headers = {"Authorization": f"Bearer {token}"}
    plants_request = requests.get(url=URL, headers=headers)
    if plants_request.ok is not True:
        raise Exception(f"Error {plants_request.status_code} contacting the api:\n")

    plants_list = plants_request.json()["plants"]

    return plants_list
