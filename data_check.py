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

    # Check sensor battery
    low_battery = [
        plant
        for plant in plants
        if plant.get("sensor", None) is not None and plant.get("sensor").get("is_battery_low", True) is True
    ]

    # Flag if any of the lists are not empty.
    for status in [thirsty, dark, hungry, low_battery]:
        if len(status) > 0:
            attention_needed = True

    return {
        "hungry": hungry,
        "dark": dark,
        "thirsty": thirsty,
        "low_battery": low_battery,
        "attention_needed": attention_needed,
    }
