# Make a dictionary containing three major rivers and the country each river
# runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'united States'}

# Use a loop to print a sentence about each river, such as The
# Nile runs through Egypt.
for k, v in rivers.items():
    print(f'\nThe {k.title()} runs throught {v.title()}.')

# Use a loop to print the name of each river included in the
# dictionary.
print(f'\nThese are the rivers mentioned:')
for k in rivers.keys():
    print(k.title())

# Use a loop to print the name of each country included in the
# dictionary.
print(f'\nThese are the countries mentioned:')
for v in rivers.values():
    print(v.title())