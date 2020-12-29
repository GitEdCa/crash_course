#age = input("What's your age? ")
#while age != 'quit':
#    age = int(age)
#    if age > 12:
#        print("Your ticket's cost is $15")
#    elif age >= 3 and age < 12:
#        print("Your ticket's cost is $10")
#    else:
#        print("Your ticket is free")
#
#    age = input("What's your age? ")
while True:
    age = input("What's your age? ")
    if age == 'quit':
        break

    age = int(age)
    if age > 12:
        print("Your ticket's cost is $15")
    elif age >= 3 and age < 12:
        print("Your ticket's cost is $10")
    else:
        print("Your ticket is free")
