houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n ** 2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)

my_list = [9, 8, 7]
new_list = [[x for x in [my_list]] for x in range(3)]
print(new_list)

my_list = [a for a in range(7)]
new_list = [a for a in range(10) if a in my_list and a % 2 == 0]
print(new_list)

my_list = ['Hello', 'World', 'Educative']
temp = [a[1].upper() for a in my_list]
print(temp)

my_list = list()
my_list.append([4, [3, 2], 1])
my_list.extend([9, 10, 11])
print(my_list[0][1][1] + my_list[2])

my_list = (8, 7, 6, 5, 4, 3, 2, 1)
print(my_list[my_list.index(3)]),
print(my_list[my_list[my_list[6] - 3] - 6])

my_list = [11, 22, 32, 17, 7]
print(my_list.pop(-3)),
my_list.remove(my_list[0]),
print(my_list)

my_tuple = (2e-04, True, False, 18, 1.7, True)
val = 0
for a in my_tuple:
    val += int(a)
print(val)

my_list = [3, 1, 2, 4]
my_tuple = ('A', 'b', 'c', 'd')
my_list.sort()
counter = 0
for a in my_tuple:
    # my_list[counter] += int(a)
    counter += 1
    break
print(my_list)

my_tuple = (4, 3, 2, 1)
# my_tuple.append((7, 6, 5))
# print len(my_tuple)

my_dict = {'Educative': 1,
           'Apple': 2,
           'Amazon': 3
           }
for (key, values) in my_dict.items():
    print(key, values)

my_dict = dict()
for i in range(3):
    for j in range(2):
        my_dict[i] = j
print(my_dict)
