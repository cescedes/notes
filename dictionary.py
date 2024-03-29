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

###########

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts) 
# and creates a song:playcount pair for each song in songs and each playcount in playcounts.
plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)
#{'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 89, 'Good Vibrations': 5}

# add a new entry
plays["Purple Haze"] = 1

# update 
plays["Respect"] = 94

# Create a dictionary called library that has two key: value pairs: 
# key "The Best Songs" with a value of plays, the dictionary you created, key "Sunday Feelings" with a value of an empty dictionary
library ={"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
#{'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}, 'Sunday Feelings': {}}

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# get the key
print(zodiac_elements["earth"])
#['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])
#['Aries', 'Leo', 'Sagittarius']
