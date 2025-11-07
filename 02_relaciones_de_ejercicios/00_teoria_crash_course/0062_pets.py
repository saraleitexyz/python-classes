# Pets: Make several dictionaries, where each dictionary represents a different pet. In
# each dictionary, include the kind of animal and the owner’s name. Store these
# dictionaries in a list called pets. Next, loop through your list and as you do, print
# everything you know about each pet.

coco = {
    'animal': 'dog',
    'owner': 'sebastian'
}

mocha = {
    'animal': 'cat',
    'owner': 'nuria'
}

mandarin = {
    'animal': 'parrot',
    'owner': 'sarah'
}

pets = [coco, mocha, mandarin]

for  pet in pets:
    print(pet)