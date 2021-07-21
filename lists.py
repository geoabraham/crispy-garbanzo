import functions

print("Random 100: {0}".format(functions.roll_dice(100)))

numbers = [1, 1, 2, 3, 5, 8, 13]
players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7"]

# players.extend(numbers) # fusiona ambas listas
players.append("Player" +
               str(len(players) + 1))  # agrega un nuevo elemento al final
players.insert(1, "Error")

players.sort()
print(players)
players.reverse()
print(players)

players.remove("Error")
players.pop()  # elimina el ultimo

players.index("Player3")

copy_of_players = players.copy()

print("Copy of Players - last player==>")
copy_of_players.pop()
print(copy_of_players)

print(numbers)
print(players)
players.clear()
print(players)

# tuples
coordinates = (4, 5)

print(coordinates[0])

# Dictionaries
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Ago": "Agost",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(months["Mar"])
print(months.get("Lol", "Not Valid Key"))

# 2D Lists
print("2D Lists")
number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
print(number_grid[1][1])
