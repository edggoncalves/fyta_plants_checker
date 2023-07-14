def check_data(plants):
    attention_needed = False

    # Check if sensor reports lack of water, sun, minerals or battery.
    thirsty = [
        plant
        for plant in plants
        if plant.get("moisture_status", 0) < 3 and plant.get("sensor", None) is not None
    ]

    dark = [
        plant
        for plant in plants
        if plant.get("light_status", 0) < 3 and plant.get("sensor", None) is not None
    ]

    hungry = [
        plant
        for plant in plants
        if plant.get("salinity_status", 0) < 3 and plant.get("sensor", None) is not None
    ]

    statuses = [thirsty, dark, hungry]

    # Flag if any of the lists are not empty.
    for status in statuses:
        if len(status) > 0:
            attention_needed = True

    return {
        "hungry": hungry,
        "dark": dark,
        "thirsty": thirsty,
        "attention_needed": attention_needed,
    }
