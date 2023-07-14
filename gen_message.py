from immutables import STATUS


def generate(statuses: dict) -> str:
    """
    Generate email body
    """
    thirsty_plants = str()
    dark_plants = str()
    hungry_plants = str()

    if len(statuses["thirsty"]) > 0:
        thirsty_plants = ", ".join(
            [plant.get("nickname") for plant in statuses["thirsty"]]
        )
        thirsty_plants = f'\t{STATUS["thirsty"]}{thirsty_plants}\n\n'

    if len(statuses["dark"]) > 0:
        dark_plants = ", ".join(
            [plant.get("nickname") for plant in statuses["dark"]]
        )
        dark_plants = f'\t{STATUS["dark"]}{dark_plants}\n\n'

    if len(statuses["hungry"]) > 0:
        hungry_plants = ", ".join(
            [plant.get("nickname") for plant in statuses["hungry"]]
        )
        hungry_plants = f'\t{STATUS["hungry"]}{hungry_plants}\n\n'

    body = "".join((thirsty_plants, dark_plants, hungry_plants))

    return body
