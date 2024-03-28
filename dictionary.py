animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)
#{'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

#create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.
zipped_drinks = zip(drinks, caffeine)

# Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through
# the zipped_drinks iterator and turns each tuple pair into a key:value item.
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
