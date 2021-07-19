# Tuple: container for values -> similar to list -> structure to store multiple pieces of information

# Create a tuple
coordinates = (4, 5)

# A tuple is immutable --> cant be changed or modified, what you see is what you get.
print(coordinates[0])

# Not possible --> because its immutable
# coordinates[1] = 10

# Tuples vs Lists
# List: square brackets [], can modify -> change, delete, add etc.
# Tuple: data that doesnt need to be changed (e.g. coordinates)

# List of tuples
coordinates2 = [(4, 5), (6, 7), (80, 34)]

print(coordinates2)
