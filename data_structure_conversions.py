# Explicit Conversion
# The template for explicitly converting from one data structure to another is as follows:
# destination_structure_name(source_structure_object)

star_wars_list = [[1, "Anakin"], [2, "Darth Vader"], [3, 1000]]
star_wars_tup = ("Obi-Wan", "Ben Kenobi", 2000)
star_wars_set = {"Master Yoda", "Old Yoda", 10000}
star_wars_dict = {1: "R2D2", 2: "C3PO", 3: 100}

print('List = ', star_wars_list)
print('Tuple = ', star_wars_tup)
print('Set = ', star_wars_set)
print('Dict = ', star_wars_dict)

# We can convert a tuple, set, or dictionary to a list
# using the list() constructor.
# In the case of a dictionary, only the keys will be converted to a list.
print(':: LISTS ::')
star_wars_list = list(star_wars_tup)  # Converting from tuple
print(f'List :: Converting from tuple :: {star_wars_list}')

star_wars_list = list(star_wars_set)  # Converting from set
print(f'List :: Converting from set :: {star_wars_list}')

star_wars_list = list(star_wars_dict)  # Converting from dictionary
print(f'List :: Converting from dictionary :: {star_wars_list}')

# We can also use the dict.items() method of a dictionary to convert it into an iterable of (key, value) tuples.
# This can further be cast into a list of tuples using list():
star_wars_list = list(star_wars_dict.items())
print(f'List :: Converting into a list of tuples :: {star_wars_list}')

print(':: TUPLES ::')

star_wars_tup = tuple(star_wars_list)  # Converting from list
print(f'Tuple :: Converting from list :: {star_wars_tup}')

star_wars_tup = tuple(star_wars_set)  # Converting from set
print(f'Tuple :: Converting from list :: {star_wars_tup}')

star_wars_tup = tuple(star_wars_dict)  # Converting from dictionary
print(f'Tuple :: Converting from list :: {star_wars_tup}')

print(':: SETS ::')
star_wars_tup = ("Obi-Wan", "Ben Kenobi", 2000)

star_wars_set = set(star_wars_list)  # Converting from list
print(f'Sets :: Converting from list :: {star_wars_set}')

star_wars_set = set(star_wars_tup)  # Converting from tuple
print(f'Sets :: Converting from list :: {star_wars_set}')

star_wars_set = set(star_wars_dict)  # Converting from dictionary
print(f'Sets :: Converting from list :: {star_wars_set}')

print(':: DICTIONARIES ::')
star_wars_tup = ((1, "Obi-Wan"), (2, "Ben Kenobi"), (3, 2000))
star_wars_set = {(1, "Master Yoda"), (2, "Old Yoda"), (3, 10000)}

star_wars_dict = dict(star_wars_list)  # Converting from list
print(f'Dict :: Converting from list :: {star_wars_dict}')

star_wars_dict = dict(star_wars_tup)  # Converting from tuple
print(f'Dict :: Converting from tuple :: {star_wars_dict}')

star_wars_dict = dict(star_wars_set)  # Converting from set
print(f'Dict :: Converting from set :: {star_wars_dict}')
