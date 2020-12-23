my_foods = ["pizza", 'falafel', 'carrot cake', 'brownie', 'pay']

print("The first three items in the list: ")
for food in my_foods[:3]:
    print(food)

print("Three items from the middle of the list are: ")
middle = len(my_foods) // 2
for food in my_foods[middle:middle + 3]:
    print(food)

print("The last three items in the list are:")
for food in my_foods[-3:]:
    print(food)

print("In reverse:")
for food in my_foods[::-1]:
    print(food)

my_foods.reverse()
print(my_foods)