from immutables import STATUS


def generate(statuses: dict) -> str:
    """
    Generate email body
    """
    thirsty_plants = str()
    dark_plants = str()
    hungry_plants = str()
    low_battery_plants = str()

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

    if len(statuses["low_battery"]) > 0:
        low_battery_plants = ", ".join(
            [plant.get("nickname") for plant in statuses["low_battery"]]
        )
        low_battery_plants = f'\t{STATUS["low_battery"]}{low_battery_plants}\n\n'

    body = "".join((thirsty_plants, dark_plants, hungry_plants, low_battery_plants))

    return body
