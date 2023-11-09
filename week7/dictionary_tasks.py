def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    for key in data:
        print(key)


def display_values(data):
    for value in data.values():
        print(value)


def display_items(data):
    for item in data.items():
        print(item)


def run():
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


run()
