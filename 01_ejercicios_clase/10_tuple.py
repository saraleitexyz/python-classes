# Tupla y acceso:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tupla de un elemento:
one_item_tuple = (3,)

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

# Although you can’t modify a tuple, you can assign a new value to a
# variable that represents a tuple. So if we wanted to change our
# dimensions, we could redefine the entire tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
