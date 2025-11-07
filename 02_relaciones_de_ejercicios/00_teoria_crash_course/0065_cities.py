# Cities: Make a dictionary called cities. Use the names of three cities as keys in
# your dictionary. Create a dictionary of information about each city and include the
# country that the city is in, its approximate population, and one fact about that city. The
# keys for each city’s dictionary should be something like country, population, and
# fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'madrid': {
        'country': 'spain',
        'population': '3 million',
        'fact': 'It has the oldest operating restaurant'
    },
    'paris': {
        'country': 'france',
        'population': '2 million',
        'fact': 'There are no stop signs in Paris.'
    },
    'rome': {
        'country': 'italy',
        'population': '4 million',
        'fact': 'The vatican has its own postal service.'
    }
}

for cities, information in cities.items():
    print(f"\n{cities.title()}'s information:")
    for k, v in information.items():
            print(f"{k}: {v}")