def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


def observed_items():
    observations = ["Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"]
    return observations


def run_task2():
    print("Counting observations...")
    local = observed_items()
    newlist = set()
    for values in local:
        newdata = local.count(values)
        tup = (values, newdata)
        newlist.add(tup)
    print(newlist)


def remove_observations(x):
    complete = False
    while complete is False:
        print("Would you like to remove observations? (Y/N)")
        check = input()
        if check == "Y":
            item = input("What would you like to remove?\n")
            x.pop(x.index(item))
            print(f"Removed {item}")
        else:
            newlist = set()
            for values in x:
                newdata = x.count(values)
                tup = (values, newdata)
                newlist.add(tup)
            print(newlist)
            complete = True

def run_task3():
    newlist = observed_items()
    remove_observations(newlist)


run_task3()
