houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)


my_list = [3, 1, 2, 4]
my_tuple = ('A', 'b', 'c', 'd')
my_list.sort()
counter = 0
for a in my_tuple:
    #my_list[counter] += int(a)
    counter += 1
    break
print(my_list)


my_tuple = (4, 3, 2, 1)
#my_tuple.append( (7, 6, 5) )
# print len(my_tuple)


my_dict = {'Educative': 1,
           'Apple': 2,
           'Amazon': 3
           }
for (key, values) in my_dict.items():
    print(key, values)
