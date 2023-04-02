import functions

print("Random 100: {0}".format(functions.roll_dice(100)))

numbers = [1, 1, 2, 3, 5, 8, 13]
players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7"]

players.extend(numbers)  # fusiona ambas listas
print(players)

players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7"]
players.insert(1, "Error")
# agrega un nuevo elemento al final
players.append("Player" + str(len(players) + 1))

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
    "Ago": "Agosto",
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

nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)

# List comprehension
nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)

# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)

x = 1
y = 1
z = 2
n = 3

permutations = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if sum((i, j, k)) != n]
print(permutations)
