def total(galleons=0, sickles=0, knuts=0):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# print(total(*coins), "Knuts")

coins_dict = {"galleons": 100, "knuts": 25}

print(total(**coins_dict), "Knuts")
